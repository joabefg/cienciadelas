import mysql.connector
from mysql.connector import Error

# Não esqueçam de importar as bibliotecas galera
# pip install flask flask-cors mysql-connector-python

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cienciadelas"
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar no banco: {e}")
        return None