from flask import Flask, jsonify, request

#obs talvez as paginas sejam mudadas ainda não sei onde ira ficar a api
app = Flask(__name__)
estoque=[
    {
    "nome":"Pizza De Mussarela",
    "quantidade":10,
    "preco":80
    },
    {
    "nome":"Pizza De Calabresa",
    "quantidade":10,
    "preco":80
    }
    ]

@app.route("/")
def inicio():
    return "Hello World!"

@app.route("/listar", methods=["GET"])
def lista():
    return jsonify(estoque)

@app.route("/add", methods=["POST"])
def adicionar():
    dados = request.get_json()
    estoque.append({
        "nome": dados["nome"],
        "quantidade": dados["quantidade"],
        "preco": dados["preco"]
    })
    return jsonify(estoque)

@app.route("/delete", methods=["DELETE"])
def deletar():
    dados = request.get_json()
    nome = dados["nome"]
    for item in estoque:
        if item["nome"] == nome:
            estoque.remove(item)
            return jsonify({"mensagem": f"{nome} removido!"})
    return jsonify({"mensagem": "Ingrediente não encontrado"}), 404

@app.route("/pedir", methods=["POST"])
def pedir():
    dados = request.get_json()
    nome = dados["nome"]
    quantidade_pedida = dados["quantidade"]  # ← pega a quantidade
    for item in estoque:
        if item["nome"] == nome:
            if item["quantidade"] >= quantidade_pedida:
                item["quantidade"] -= quantidade_pedida  # ← diminui a quantidade certa
                return jsonify({"mensagem": f"Pedido de {nome} realizado!"})
            else:
                return jsonify({"mensagem": "Sem estoque suficiente!"}), 400
    return jsonify({"mensagem": "Pizza não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)