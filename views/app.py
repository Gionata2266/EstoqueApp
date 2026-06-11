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

def buscar_pizza():
    response = requests.get(f"{API_URL}/listar") #salva em igredientes
    ingredientes = response.json()
    
    listar.delete("1.0", tk.END)  # limpa o Text quando clica em mostar os igrediente para não ficar aparecendo
    for item in ingredientes:    #mostra os igrendientes que foram salvos todos
        listar.insert(tk.END, f"{item['nome']} - Qtd: {item['quantidade']} - R${item['preco']}\n")   
#########################


def deletar_pizza():
    nome = entrada_nome.get()
    if nome == "":
        messagebox.showwarning("Aviso!", "Preencha o campo Nome para deletar")
    else:
        requests.delete(f"{API_URL}/delete", json={"nome": nome})
        messagebox.showinfo("Sucesso!", f"{nome} deletado!")
        buscar_pizza()

def pedir_pizza():
    pizza = entrada_pizza.get()
    quantidade = int(entrada_quantidade_pedido.get())
    if pizza == "":
        messagebox.showwarning("Aviso!", "Preencha o campo Pizza")
    else:
        response = requests.post(f"{API_URL}/pedir", json={"nome": pizza, "quantidade": quantidade})
        if response.status_code == 200:
            messagebox.showinfo("Sucesso!", f"Pedido realizado!")
            buscar_pizza()
        else:
            messagebox.showwarning("Aviso!", "Pizza não encontrada ou sem estoque!")



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

listar = tk.Text(janela, height=15, width=50)
listar.pack(padx=5)


frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_buscar = ttk.Button(frame_botoes, text="Pizzas Disponiveis", command=buscar_pizza)
botao_buscar.grid(row=0, column=0, padx=5)

botao_deletar = ttk.Button(frame_botoes, text="Deletar", command=deletar_pizza)
botao_deletar.grid(row=0, column=1, padx=5)

ttk.Label(janela, text="Digite Sua Pizza:").pack(pady=5)
entrada_pizza = ttk.Entry(janela, width=30)
entrada_pizza.pack(pady=5)

ttk.Label(janela, text="Quantidade:").pack(pady=5)
entrada_quantidade_pedido = ttk.Entry(janela, width=30)
entrada_quantidade_pedido.pack(pady=5)

botao_pedido = ttk.Button(janela, text="Pedir", command=pedir_pizza)
botao_pedido.pack(pady=5)

janela.mainloop()