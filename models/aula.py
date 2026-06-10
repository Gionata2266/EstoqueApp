class Estoque:
    def __init__(self,nome,quantidade,preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    print("Tabela")
    
    def Informacoes(self):
        print(f"Produto: {self.nome} Quantidade: {self.quantidade} Preco: {self.preco}")
        
estoque1 = Estoque("mussarela",10,5)

estoque1.Informacoes()

