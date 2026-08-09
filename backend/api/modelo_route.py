from flask import Blueprint, request, jsonify
from config import conectar

modelo_bp = Blueprint("modelo_bp", __name__)


@modelo_bp.route("/api/modelo", methods=["GET"])
def listar_modelos():
    conexao = conectar()
    if not conexao:
        return jsonify({"erro": "Falha na conexão com o banco"}), 500

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modelo")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()

    return jsonify(resultado), 200


@modelo_bp.route("/api/modelo/<int:id>", methods=["GET"])
def buscar_modelo(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modelo WHERE id = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200


@modelo_bp.route("/api/modelo", methods=["POST"])
def criar_modelo():
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO modelo (atributo) VALUES (%s)",
        (dados["atributo"],)
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()

    return jsonify({"id": novo_id, "atributo": dados["atributo"]}), 201


@modelo_bp.route("/api/modelo/<int:id>", methods=["PUT"])
def atualizar_modelo(id):
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE modelo SET atributo = %s WHERE id = %s",
        (dados["atributo"], id)
    )
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()

    if linhas_afetadas == 0:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({"id": id, "atributo": dados["atributo"]}), 200


@modelo_bp.route("/api/modelo/<int:id>", methods=["DELETE"])
def deletar_modelo(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM modelo WHERE id = %s", (id,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()

    if linhas_afetadas == 0:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({"mensagem": "Removido com sucesso"}), 200