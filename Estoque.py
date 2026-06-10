from flask import Flask, jsonify
#obs talvez as paginas sejam mudadas ainda não sei onde ira ficar a api
app = Flask(__name__)

class Estoque:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

estoque = Estoque("mussarela", 10, 5)

@app.route("/")
def inicio():
    return "Hello World!"

@app.route("/estoque")
def lista_estoque():
    return jsonify({
        "nome": estoque.nome,
        "quantidade": estoque.quantidade,
        "preco": estoque.preco
    })

if __name__ == "__main__":
    app.run(debug=True)