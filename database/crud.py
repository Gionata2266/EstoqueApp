import sqlite3 

conexao = sqlite3.connect("database.db", check_same_thread=False)
cursor = conexao.cursor()