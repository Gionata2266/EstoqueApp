from database.conexao import conexao, cursor 

class Estoque:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()
        self._criar_tabela() 

    def _criar_tabela(self):
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            marca TEXT NOT NULL,
            unidade_medida TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL,
            data_validade DATE NOT NULL
            )
        """)
        self.conexao.commit()

    def inserir_item(nome, categoria, marca, unidade_medida, quantidade, preco, data_validade):
        cursor.execute("""
            INSERT INTO estoque(nome, categoria, marca, unidade_medida, quantidade, preco, data_validade) 
            VALUES(?,?,?,?,?,?,?)
        """, (nome, categoria, marca, unidade_medida, quantidade, preco, data_validade))
        conexao.commit()

    def listar_itens():
        cursor.execute("SELECT id, nome, categoria, marca, unidade_medida, quantidade, preco, data_validade FROM estoque")
        return cursor.fetchall()

    def atualizar_item(id, nome, categoria, marca, unidade_medida, quantidade, preco, data_validade):
        cursor.execute("""
            UPDATE estoque SET
            nome = ?, categoria = ?, marca = ?, unidade_medida = ?, quantidade = ?, preco = ?, data_validade = ? 
            WHERE id = ?
        """, (nome, categoria, marca, unidade_medida, quantidade, preco, data_validade, id))
        conexao.commit()

    def deletar_item(id):
        cursor.execute("DELETE FROM estoque WHERE id = ?", (id,))
        conexao.commit()