from flask import Blueprint, request, jsonify
from config import conectar

cartas_bp = Blueprint("cartas_bp", __name__)

@cartas_bp.route("/api/cartas", methods=["GET"])
def listar_cartass():
    conexao = conectar()
    if not conexao:
        return jsonify({"erro": "Falha na conexão com o banco"}), 500

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cartas")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()

    return jsonify(resultado), 200


@cartas_bp.route("/api/cartas/<int:id>", methods=["GET"])
def buscar_cartas(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cartas WHERE id = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200


@cartas_bp.route("/api/cartas", methods=["POST"])
def criar_cartas():
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO cartas (atributo) VALUES (%s)",
        (dados["atributo"],)
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()

    return jsonify({"id": novo_id, "atributo": dados["atributo"]}), 201


@cartas_bp.route("/api/cartas/<int:id>", methods=["PUT"])
def atualizar_cartas(id):
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE cartas SET atributo = %s WHERE id = %s",
        (dados["atributo"], id)
    )
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()

    if linhas_afetadas == 0:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({"id": id, "atributo": dados["atributo"]}), 200


@cartas_bp.route("/api/cartas/<int:id>", methods=["DELETE"])
def deletar_cartas(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM cartas WHERE id = %s", (id,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()

    if linhas_afetadas == 0:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({"mensagem": "Removido com sucesso"}), 200