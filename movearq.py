import os
import paramiko
import time

def transferir_arquivos():
    host = '192.168.15.7'
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

        if 'dadosvendas' in sftp.listdir(caminho_destino_linux):
            with sftp.open(caminho_arquivo_destino, 'a') as arquivo_destino, open(caminho_arquivo_origem, 'r') as arquivo_origem:
                for linha in arquivo_origem:
                    arquivo_destino.write(linha)

            os.remove(caminho_arquivo_origem)        


        else:
            sftp.put(caminho_arquivo_origem, caminho_arquivo_destino)

            sftp.rename(caminho_arquivo_destino, os.path.join(caminho_destino_linux, 'dadosvendas'))

            os.remove(caminho_arquivo_origem)

    sftp.close()
    ssh_client.close()    

while True:

    transferir_arquivos()
    time.sleep(2)