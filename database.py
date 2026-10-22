import sqlite3

def conectar():
    return sqlite3.connnect("eventos.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teste (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            numero INTEGER NOT NULL,
            data DATE NOT NULL
        )
    """)
    conexao.commit()
    cursor.close()
    conexao.close()