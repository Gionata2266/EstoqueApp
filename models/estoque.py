class Estoque:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = conexao.cursor()

    def _criar_tabela(self):
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS estoque (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL UNIQUE,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
            )
        """)
        self.conexao.commit()

    def inserir_item(self, nome, quantidade, preco):
        self.cursor.execute("SELECT id, quantidade FROM estoque WHERE nome = ?", (nome,)) #procura pelo nome
        existente = self.cursor.fetchone() #pega os dados da busca se o dado nome existir
        
        if existente: #se o dado nome existir
            nova_quantidade = existente["quantidade"] + quantidade #ele vai pegar quantidade nova e vai colocar na que ja tem 
            self.cursor.execute("UPDATE estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, existente["id"])) #atualiza o banco 
        else:#se não encontrou nenhum item ele vai adicionar normal como padrão
            self.cursor.execute("""
                INSERT INTO estoque(nome, quantidade, preco) 
                VALUES(?,?,?)
            """, (nome, quantidade, preco))
        
        self.conexao.commit()

    def listar_itens(self):
        self.cursor.execute("SELECT id, nome, quantidade, preco FROM estoque")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def atualizar_item(self, id, nome, quantidade, preco):
        self.cursor.execute("""
            UPDATE estoque SET
            nome = ?, quantidade = ?, preco = ?
            WHERE id = ?
        """, (nome, quantidade, preco, id))
        self.conexao.commit()

    def deletar_item(self, id):
        self.cursor.execute("DELETE FROM estoque WHERE id = ?", (id,))
        self.conexao.commit()
        
    def buscar_por_id(self, id):
        self.cursor.execute("SELECT * FROM estoque WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None
    
    def atualizar_quantidade(self, id, nova_quantidade):
        self.cursor.execute(
            "UPDATE estoque SET quantidade = ? WHERE id = ?",
            (nova_quantidade, id)
        )
        
        
        
        
        self.conexao.commit()