import subprocess

def executar_comando(comando, entrada=None):
    """Executa um comando no shell e retorna a saída."""
    print(f"Executando comando: {comando}")
    process = subprocess.Popen(comando, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate(input=entrada)
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, comando, output=output, stderr=error)
    return output

# Pedir a porta de pareamento, código de pareamento e porta de conexão
porta_pareamento = input('Qual a porta de pareamento? ')
codigo_pareamento = input('Qual o código de pareamento? ')
porta_conexao = input('Agora digite a porta de conexão: ')

try:
    # Parear o dispositivo
    pair_command = f'adb pair localhost:{porta_pareamento}'
    pair_output = executar_comando(pair_command, entrada=codigo_pareamento + '\n')
    print(pair_output)
    print(f'Pareamento com localhost:{porta_pareamento} realizado com sucesso.')

    # Conectar ao dispositivo
    connect_command = f'adb connect localhost:{porta_conexao}'
    connect_output = executar_comando(connect_command)
    print(connect_output)
    print(f'Conexão com localhost:{porta_conexao} realizada com sucesso.')

    # Realizar hard reset
    hard_reset_command = 'adb shell recovery --wipe_data'
    hard_reset_output = executar_comando(hard_reset_command)
    print(hard_reset_output)
    print('Dispositivo formatado com sucesso (hard reset realizado).')

except subprocess.CalledProcessError as e:
    print(f'Erro ao executar o comando: {e.cmd}')
    print(f'Código de retorno: {e.returncode}')
    print(f'Saída: {e.output}')
    print(f'Erro: {e.stderr}')