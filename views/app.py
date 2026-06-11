import tkinter as tk
from tkinter import ttk, messagebox
import requests          

API_URL = "http://127.0.0.1:5000"  


def mostrar():
    nome = entrada_nome.get()
    if nome =="":
        messagebox.showwarning("Aviso!","Prencha o Campo Nome")
    else:
        messagebox.showwarning("Sucesso!",f"Usuario:{nome} Cadastrado!")    

def buscar_ingredientes():
    response = requests.get(f"{API_URL}/listar")
    ingredientes = response.json()
    
    listar.delete("1.0", tk.END)  # limpa o Text antes
    for item in ingredientes:
        listar.insert(tk.END, f"{item['nome']} - Qtd: {item['quantidade']} - R${item['preco']}\n")   
#########################
janela = tk.Tk()
janela.title("Cadastro De Usuario")
janela.geometry("300x200")

label_nome = ttk.Label(janela, text="Nome:")# criando input com nome
label_nome.pack(pady=5) #distanci

entrada_nome = ttk.Entry(janela, width=30)  
entrada_nome.pack(pady=5)

botao = ttk.Button(janela, text="Cadastrar",command=mostrar)
botao.pack(pady=10)

listar = tk.Text(janela,height=10,width=30)
listar.pack(padx=5)

botao_buscar = ttk.Button(janela, text="Buscar Ingredientes", command=buscar_ingredientes)
botao_buscar.pack(pady=5)



janela.mainloop()