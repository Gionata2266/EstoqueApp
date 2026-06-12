import tkinter as tk
from tkinter import ttk, messagebox
import requests          

API_URL = "http://127.0.0.1:5000"  


def cadastrar_pizza():
    nome = entrada_nome.get()
    if nome =="":
        messagebox.showwarning("Aviso!","Prencha o Campo Nome")
    else:
        dados = {
            "nome": entrada_nome.get(),
            "quantidade": int(entrada_quantidade.get()),
            "preco": float(entrada_preco.get())
        }
        requests.post(f"{API_URL}/add", json=dados)
        messagebox.showinfo("Sucesso!", "Ingrediente cadastrado!")
        buscar_pizza()   

def buscar_pizza():
    response = requests.get(f"{API_URL}/listar") #salva em igredientes
    ingredientes = response.json()
    
    response = requests.get(f"{API_URL}/listar")
    ingredientes = response.json()
    
    listar.delete(*listar.get_children())  # limpa a tabela
    for item in ingredientes: #mostra os igrendientes que foram salvos todos
        listar.insert("", tk.END, values=(item["id"], item["nome"], item["quantidade"], item["preco"]))
      
#########################


def deletar_pizza():
    selecionado = listar.selection()
    if not selecionado:
        messagebox.showwarning("Aviso!", "Selecione um item na lista para deletar")
        return
    
    item = listar.item(selecionado)
    id_item = item["values"][0]
    
    requests.delete(f"{API_URL}/delete", json={"id": id_item})
    messagebox.showinfo("Sucesso!", "Item deletado!")
    buscar_pizza()

def pedir_pizza():
    selecionado = listar.selection()
    if not selecionado:
        messagebox.showwarning("Aviso!", "Selecione um item na lista para pedir")
        return
    
    if entrada_quantidade_pedido.get() == "":
        messagebox.showwarning("Aviso!", "Digite a quantidade da retirada")
        return
    
    item = listar.item(selecionado)
    id_item = item["values"][0]
    quantidade = int(entrada_quantidade_pedido.get())
    
    response = requests.post(f"{API_URL}/pedir", json={"id": id_item, "quantidade": quantidade})
    if response.status_code == 200:
        messagebox.showinfo("Sucesso!", "Pedido realizado!")
        buscar_pizza()
    else:
        messagebox.showwarning("Aviso!", "Sem estoque suficiente!")



janela = tk.Tk()
janela.title("Cadastro De Pizza")
janela.geometry("1000x650")

ttk.Label(janela, text="Nome:").pack(pady=5)
entrada_nome = ttk.Entry(janela, width=30)
entrada_nome.pack(pady=5)

ttk.Label(janela, text="Quantidade:").pack()
entrada_quantidade = ttk.Entry(janela, width=30)
entrada_quantidade.pack(pady=5)

ttk.Label(janela, text="Preço:").pack()
entrada_preco = ttk.Entry(janela, width=30)
entrada_preco.pack(pady=5)

ttk.Button(janela, text="Cadastrar Pizza", command=cadastrar_pizza).pack(pady=5)

listar = ttk.Treeview(janela, columns=("id", "nome", "qtd", "preco"), show="headings")
listar.heading("id", text="ID")
listar.heading("nome", text="Nome")
listar.heading("qtd", text="Quantidade")
listar.heading("preco", text="Preço")

listar.column("id", width=40)
listar.column("nome", width=200)
listar.column("qtd", width=80)
listar.column("preco", width=80)

listar.pack(pady=5)


frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_buscar = ttk.Button(frame_botoes, text="Pizzas Disponiveis", command=buscar_pizza)
botao_buscar.grid(row=0, column=0, padx=5)

botao_deletar = ttk.Button(frame_botoes, text="Deletar", command=deletar_pizza)
botao_deletar.grid(row=0, column=1, padx=5)

ttk.Label(janela, text="Quantidade:").pack(pady=5)
entrada_quantidade_pedido = ttk.Entry(janela, width=30)
entrada_quantidade_pedido.pack(pady=5)

botao_pedido = ttk.Button(janela, text="Pedir", command=pedir_pizza)
botao_pedido.pack(pady=5)

janela.mainloop()