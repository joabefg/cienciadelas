from config import conectar
# ==========================================
# VERSÃO TEMPORÁRIA
# Troque o conteúdo deste arquivo quando o
# SQL da tabela "modelo" estiver pronto
# ==========================================

_dados = []
_proximo_id = 1


def listar_todos():
    return _dados


def buscar_por_id(id):
    """
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modelo WHERE id = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado
    """
    return next((item for item in _dados if item["id"] == id), None)


def criar(atributo):
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO modelo (atributo) VALUES (%s)", (atributo,))
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()
    return {"id": novo_id, "atributo": atributo}
    """
    global _proximo_id
    novo = {"id": _proximo_id, "atributo": atributo}
    _dados.append(novo)
    _proximo_id += 1
    return novo


def atualizar(id, atributo):
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE modelo SET atributo = %s WHERE id = %s", (atributo, id))
    conexao.commit()
    linhas = cursor.rowcount
    cursor.close()
    conexao.close()
    return {"id": id, "atributo": atributo} if linhas > 0 else None
    """
    item = buscar_por_id(id)
    if item:
        item["atributo"] = atributo
    return item


def deletar(id):
    """
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM modelo WHERE id = %s", (id,))
    conexao.commit()
    linhas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas > 0
    """
    global _dados
    tamanho_antes = len(_dados)
    _dados = [item for item in _dados if item["id"] != id]
    return len(_dados) < tamanho_antes