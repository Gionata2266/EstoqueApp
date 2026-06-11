from flask import Flask, jsonify, request

#obs talvez as paginas sejam mudadas ainda não sei onde ira ficar a api
app = Flask(__name__)
estoque=[
    {
    "nome":"Mussarela",
    "quantidade":10,
    "preco":2000
    },
    {
    "nome":"Molho de tomate",
    "quantidade":10,
    "preco":2000
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


if __name__ == "__main__":
    app.run(debug=True)