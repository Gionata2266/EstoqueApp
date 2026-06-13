from flask import Flask
from controllers.Api import estoque_bp
from database.conexao import get_conexao
from models.estoque import Estoque

app = Flask(__name__)
app.register_blueprint(estoque_bp)

conn = get_conexao()
estoque = Estoque(conn)
estoque._criar_tabela()

if __name__ == "__main__":
    app.run(debug=True)