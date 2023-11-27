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


data_atual = datetime.now().strftime('%Y-%m-%d')


nome_arquivo = f"dadosvendas_{data_atual}.txt"


caminho = r"C:\Users\keysson\Documents\dados_extraidos\\" + nome_arquivo  # Substitua 'keysson' pelo seu nome de usuário


with open(caminho, "w") as arquivo:
    for linha in cursor.fetchall():
        arquivo.write(str(linha) + "\n")


    

cursor.close()
conexao.close()

time.sleep(1)