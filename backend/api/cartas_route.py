from flask import Blueprint, request, jsonify
from config import conectar
from repositorios import cartas_repository as repo

cartas_bp = Blueprint("cartas_bp", __name__)

@cartas_bp.route("/api/cartas", methods=["GET"])
def listar_cartas():
    return jsonify(repo.listar_todos()), 200



@cartas_bp.route("/api/cartas/<int:id>", methods=["GET"])
def buscar_cartas(id):
    resultado = repo.buscar_por_id(id)

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200


@cartas_bp.route("/api/cartas", methods=["POST"])
def criar_cartas():
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    item_criado = repo.criar(dados["atributo"])
    # item_criado = repo.criar(dados["matricula"], dados["nome"], dados["idade"])
    return jsonify(item_criado), 201


@cartas_bp.route("/api/cartas/<int:id>", methods=["PUT"])
def atualizar_cartas(id):
    dados = request.get_json()

    if not dados or "atributo" not in dados:
        return jsonify({"erro": "atributo é obrigatório"}), 400

    resultado = repo.atualizar(id, dados["atributo"])

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200


@cartas_bp.route("/api/cartas/<int:id>", methods=["DELETE"])
def deletar_cartas(id):
    removido = repo.deletar(id)

    if not removido:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({"mensagem": "Removido com sucesso"}), 200