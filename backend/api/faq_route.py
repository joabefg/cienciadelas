from flask import Blueprint, request, jsonify, render_template
from controllers import faq_controller
from repositorios import faq_model

faq_bp = Blueprint("faq_bp", __name__)


@faq_bp.route("/faq", methods=["GET"])
def pagina_faq():
    perguntas = faq_controller.listar_perguntas()
    return render_template("faq.html", perguntas=perguntas)


@faq_bp.route("/api/faq", methods=["GET"])
def listar_faq():
    perguntas = faq_controller.listar_perguntas()
    return jsonify(perguntas), 200


@faq_bp.route("/api/faq", methods=["POST"])
def criar_faq():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados obrigatórios"}), 400

    pergunta = dados.get("pergunta")
    resposta = dados.get("resposta")

    resultado = faq_controller.cadastrar_pergunta(
        pergunta, resposta
    )

    if not resultado:
        return jsonify({"erro": "Pergunta e resposta são obrigatórias"}), 400

    return jsonify(resultado), 201