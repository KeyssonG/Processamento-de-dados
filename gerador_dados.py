import pyodbc
from faker import Faker
import random
import time



dados_conexao = (
    "Driver={SQL Server};"
    "Server=;"
    "Database=vendas_teste;"
    "Trusted_Connection=yes;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

fake = Faker()

produtos = ['camisa', 'celular', 'sapato', 'tênis', 'relógio', 'mochila', 'bermuda']

for _ in range(50):
    ID = str(random.randint(1, 99999)).zfill(5)
    nome = fake.name()
    data_venda = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    produto = random.choice(produtos)
    valor = round(random.uniform(10.0, 1000.0), 2)

    query = "INSERT INTO vendas (ID, nome, data_venda, produto, valor) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (ID, nome, data_venda, produto, valor))
    conexao.commit()

    time.sleep(2)

conexao.close()    
