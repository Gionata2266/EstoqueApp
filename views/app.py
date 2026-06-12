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
        messagebox.showinfo("Sucesso!", "Pizza cadastrada!")
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

def editar_pizza(event):
    selecionado = listar.selection()
    if not selecionado:
        return
    
    item = listar.item(selecionado)
    id_item = item["values"][0]
    nome_atual = item["values"][1]
    qtd_atual = item["values"][2]
    preco_atual = item["values"][3]
    
    # janela de edição
    janela_edit = tk.Toplevel(janela)
    janela_edit.title("Editar Item")
    janela_edit.geometry("300x250")
    
    ttk.Label(janela_edit, text="Nome:").pack(pady=5)
    entrada_edit_nome = ttk.Entry(janela_edit, width=30)
    entrada_edit_nome.insert(0, nome_atual)
    entrada_edit_nome.pack(pady=5)
    
    ttk.Label(janela_edit, text="Quantidade:").pack()
    entrada_edit_qtd = ttk.Entry(janela_edit, width=30)
    entrada_edit_qtd.insert(0, qtd_atual)
    entrada_edit_qtd.pack(pady=5)
    
    ttk.Label(janela_edit, text="Preço:").pack()
    entrada_edit_preco = ttk.Entry(janela_edit, width=30)
    entrada_edit_preco.insert(0, preco_atual)
    entrada_edit_preco.pack(pady=5)
    
    def salvar_edicao():
        dados = {
            "id": id_item,
            "nome": entrada_edit_nome.get(),
            "quantidade": int(entrada_edit_qtd.get()),
            "preco": float(entrada_edit_preco.get())
        }
        requests.put(f"{API_URL}/editar", json=dados)
        janela_edit.destroy()
        buscar_pizza()
    
    ttk.Button(janela_edit, text="Salvar", command=salvar_edicao).pack(pady=10)


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
listar.bind("<Double-1>", editar_pizza)


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