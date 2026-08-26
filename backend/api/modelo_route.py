from flask import Blueprint, request, jsonify
from config import conectar
from repositorios import modelo_repository as repo


modelo_bp = Blueprint("modelo_bp", __name__)


@modelo_bp.route("/api/modelo", methods=["GET"])
def listar_modelos():
    return jsonify(repo.listar_todos()), 200


@modelo_bp.route("/api/modelo/<int:id>", methods=["GET"])
def buscar_modelo(id):
    resultado = repo.buscar_por_id(id)

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200


@modelo_bp.route("/api/modelo", methods=["POST"])
def criar_modelo():
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    item_criado = repo.criar(dados["atributo"])
    return jsonify(item_criado), 201


@modelo_bp.route("/api/modelo/<int:id>", methods=["PUT"])
def atualizar_modelo(id):
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    resultado = repo.atualizar(id, dados["atributo"])

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200


@modelo_bp.route("/api/modelo/<int:id>", methods=["DELETE"])
def deletar_modelo(id):
    removido = repo.deletar(id)

    if not removido:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({"mensagem": "Removido com sucesso"}), 200