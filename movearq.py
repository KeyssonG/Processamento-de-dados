import os
import paramiko
import time

def transferir_arquivos():
    host = '192.168.15.6'
    port = 22
    username = 'keysson'
    password = '251299'

    caminho_origem_windows = r'C:\Users\keysson\Documents\dados_extraidos'

    caminho_destino_linux = '/home/keysson/teste_rotina/IN/'

    arquivos = os.listdir(caminho_origem_windows)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    sftp =ssh_client.open_sftp()

    for arquivo in arquivos:
        caminho_arquivo_origem = os.path.join(caminho_origem_windows, arquivo)
        caminho_arquivo_destino = os.path.join(caminho_destino_linux, arquivo)

        sftp.put(caminho_arquivo_origem, caminho_arquivo_destino)

        os.remove(caminho_arquivo_origem)

    sftp.close()
    ssh_client.close()    

while True:

    transferir_arquivos()
    time.sleep(5)