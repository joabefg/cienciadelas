from flask import Blueprint, request, jsonify
from config import conectar

personagens_bp = Blueprint("personagens_bp", __name__)

@personagens_bp.route("/api/v1/personagens", methods = ["GET"])
def listar_personagenss():

    conexao = conectar()
    if not conexao :
        return jsonify({"erro": "Falha na conexão com banco "}), 500
    
    cursor = conexao.cursor(dictionary = True)
    cursor.execute("SELECT * FROM personagens")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()

    return jsonify(resultado) , 200 

@personagens_bp.route("/api/v1/personagens/<int:id>", methods=["GET"])
def buscar_personagens(id):
    conexao = conectar()
    
    if not conexao :
     return jsonify({"erro": "Falha na conexão com banco "}), 500

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM personagens WHERE id = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()

    if not resultado:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(resultado), 200
@personagens_bp.route("/api/v1/personagens", methods=["POST"])
def criar_personagem():
    dados = request.get_json()

    campos_obrigatorios = ["nome_personagem", "descricao_personagem", "biografia_personagem"]
    faltando = [c for c in campos_obrigatorios if c not in (dados or {})]
    if faltando:
        return jsonify({"erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"}), 400

    limites = {
        "nome_personagem": 50,
        "descricao_personagem": 255,
        "biografia_personagem": 300,
    }

    for campo, limite in limites.items():
        valor = dados[campo]
        if not isinstance(valor, str) or not valor.strip():
            return jsonify({"erro": f"{campo} deve ser um texto não vazio"}), 400
        if len(valor) > limite:
            return jsonify({
                "erro": f"{campo} excede o limite de {limite} caracteres (recebido: {len(valor)})"
            }), 400

    conexao = conectar()
    if not conexao:
        return jsonify({"erro": "Falha na conexão com banco "}), 500

    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO personagens (Nome_personagem, Descricao_personagem, Biografia_personagem)
        VALUES (%s, %s, %s)
        """,
        (
            dados["nome_personagem"],
            dados["descricao_personagem"],
            dados["biografia_personagem"],
        )
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    conexao.close()

    return jsonify({
        "id": novo_id,
        "nome_personagem": dados["nome_personagem"],
        "descricao_personagem": dados["descricao_personagem"],
        "biografia_personagem": dados["biografia_personagem"],
    }), 201


@personagens_bp.route("/api/v1/personagens/<int:id>", methods=["PUT"])
def atualizar_personagem(id):
    dados = request.get_json()

    campos_obrigatorios = ["nome_personagem", "descricao_personagem", "biografia_personagem"]
    faltando = [c for c in campos_obrigatorios if c not in (dados or {})]
    if faltando:
        return jsonify({"erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"}), 400

    limites = {
        "nome_personagem": 50,
        "descricao_personagem": 255,
        "biografia_personagem": 300,
    }

    for campo, limite in limites.items():
        valor = dados[campo]
        if not isinstance(valor, str) or not valor.strip():
            return jsonify({"erro": f"{campo} deve ser um texto não vazio"}), 400
        if len(valor) > limite:
            return jsonify({
                "erro": f"{campo} excede o limite de {limite} caracteres (recebido: {len(valor)})"
            }), 400

    conexao = conectar()
    if not conexao:
        return jsonify({"erro": "Falha na conexão com banco "}), 500

    cursor = conexao.cursor()
    cursor.execute(
        """
        UPDATE personagens
        SET Nome_personagem = %s, Descricao_personagem = %s, Biografia_personagem = %s
        WHERE id = %s
        """,
        (
            dados["nome_personagem"],
            dados["descricao_personagem"],
            dados["biografia_personagem"],
            id,
        )
    )
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()

    if linhas_afetadas == 0:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify({
        "id": id,
        "nome_personagem": dados["nome_personagem"],
        "descricao_personagem": dados["descricao_personagem"],
        "biografia_personagem": dados["biografia_personagem"],
    }), 200