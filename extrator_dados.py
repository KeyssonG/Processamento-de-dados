import pyodbc
from datetime import datetime
import time


conexao = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-5SNUTLQ;"  
    "Database=vendas_teste;"
    "Trusted_Connection=yes;"
)


query = "SELECT * FROM vendas"


cursor = conexao.cursor()
cursor.execute(query)



nome_arquivo = f"dadosvendas.txt"


caminho = r"C:\Users\keysson\Documents\dados_extraidos\\" + nome_arquivo


with open(caminho, "w") as arquivo:
    for linha in cursor.fetchall():
        arquivo.write(str(linha) + "\n")


    

cursor.close()
conexao.close()

time.sleep(1)