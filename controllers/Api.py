from flask import Blueprint, jsonify, request
from models.estoque import Estoque
from database.conexao import get_conexao

estoque_bp = Blueprint("estoque", __name__)

@estoque_bp.route("/")
def inicio():
    return "Hello World!"

@estoque_bp.route("/listar", methods=["GET"])
def lista():
    conn = get_conexao()
    estoque = Estoque(conn)
    resultado = estoque.listar_itens()
    conn.close()
    return jsonify(resultado)

@estoque_bp.route("/add", methods=["POST"])
def adicionar():
    conn = get_conexao()
    estoque = Estoque(conn)
    dados = request.get_json()
    estoque.inserir_item(
        dados["nome"], 
        dados["quantidade"],
        dados["preco"]
    )
    conn.close()
    return jsonify(estoque)

@estoque_bp.route("/delete", methods=["DELETE"])
def deletar():
    dados = request.get_json()
    conn = get_conexao()
    estoque = Estoque(conn)
    item = estoque.buscar_por_id(dados["id"])
    
    if not item:
        conn.close()
        return jsonify({"mensagem": "Item não encontrado"}), 404
    
    estoque.deletar_item(dados["id"])
    conn.close()
    return jsonify({"mensagem": "Item removido!"})

@estoque_bp.route("/pedir", methods=["POST"])
def pedir():
    dados = request.get_json()
    conn = get_conexao()
    estoque = Estoque(conn)
    
    item = estoque.buscar_por_id(dados["id"])
    
    if not item:
        conn.close()
        return jsonify({"mensagem": "Item não encontrado"}), 404
    
    if item["quantidade"] < dados["quantidade"]:
        conn.close()
        return jsonify({"mensagem": "Sem estoque suficiente!"}), 400
    
    nova_quantidade = item["quantidade"] - dados["quantidade"]
    estoque.atualizar_quantidade(dados["id"], nova_quantidade)
    conn.close()
    return jsonify({"mensagem": "Pedido realizado!"})
    
