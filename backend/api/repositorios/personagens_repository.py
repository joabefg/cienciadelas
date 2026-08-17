from config import conectar

dados = []
_proximo_id = 1

def listar_todos ():
    return _dados

def listar_personagens(id):
    """
    cursor = conexao.cursor(dictionary = True)
    cursor.execute("SELECT * FROM personagens")
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(resultado) , 200 
    """
    return next((item for item in _dados if item ["id"] == id),None)

def buscar_personagens(id):
    """
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
    """

def criar_personagens(id,atributo):
"""
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
        
        INSERT INTO personagens (Nome_personagem, Descricao_personagem, Biografia_personagem)
        VALUES (%s, %s, %s)
        ,
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
"""
   global _proximo_id
    novo = {"id": _proximo_id, "atributo": "nome_personagens","biografia_personagens", "descrição_personagens"}
    _dados.append(novo)
    _proximo_id += 1
    return novo

def  atualizar_personagem(id): 
    """
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
        
        UPDATE personagens
        SET Nome_personagem = %s, Descricao_personagem = %s, Biografia_personagem = %s
        WHERE id = %s
        ,
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
    """

    item = buscar_por_id(id)
    if item:
        item["atributo"] = atributo
    return item
