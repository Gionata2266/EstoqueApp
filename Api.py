from flask import Flask, jsonify
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

@app.route("/listar")
def lista():
    return jsonify(estoque)

@app.route("/add")
def adicionar():
    estoque.append({"nome":"calabresa", "quantidade":10,"preco":8})
    return jsonify(estoque)


if __name__ == "__main__":
    app.run(debug=True)