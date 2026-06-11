import tkinter as tk
from tkinter import ttk, messagebox
import requests          

API_URL = "http://127.0.0.1:5000"  


def cadastro_ingredientes():
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

def buscar_ingredientes():
    response = requests.get(f"{API_URL}/listar") #salva em igredientes
    ingredientes = response.json()
    
    listar.delete("1.0", tk.END)  # limpa o Text quando clica em mostar os igrediente para não ficar aparecendo
    for item in ingredientes:    #mostra os igrendientes que foram salvos todos
        listar.insert(tk.END, f"{item['nome']} - Qtd: {item['quantidade']} - R${item['preco']}\n")   
#########################




janela = tk.Tk()
janela.title("Cadastro De Ingrediente")
janela.geometry("400x400")

ttk.Label(janela, text="Nome:").pack(pady=5)
entrada_nome = ttk.Entry(janela, width=30)
entrada_nome.pack(pady=5)

ttk.Label(janela, text="Quantidade:").pack()
entrada_quantidade = ttk.Entry(janela, width=30)
entrada_quantidade.pack(pady=5)

ttk.Label(janela, text="Preço:").pack()
entrada_preco = ttk.Entry(janela, width=30)
entrada_preco.pack(pady=5)

ttk.Button(janela, text="Cadastrar Ingrediente", command=cadastro_ingredientes).pack(pady=5)

listar = tk.Text(janela, height=10, width=30)
listar.pack(padx=5)

botao_buscar = ttk.Button(janela, text="Buscar Ingredientes", command=buscar_ingredientes)
botao_buscar.pack(pady=5)

janela.mainloop()