from config import conectar


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def listar_todos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM faq")
    resultados = cursor.fetchall()

    perguntas = [
        {
            "id": item[0],
            "pergunta": item[1],
            "resposta": item[2]
        }
        for item in resultados
    ]

    conexao.close()
    return perguntas


def criar(pergunta, resposta):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO faq (pergunta, resposta) VALUES (?, ?)",
        (pergunta, resposta)
    )

    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return {
        "id": novo_id,
        "pergunta": pergunta,
        "resposta": resposta
    }