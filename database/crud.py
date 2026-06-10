import sqlite3 

conexao = sqlite3.connect("database.db", check_same_thread=False)
cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXIST estoque(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    )
    """
    
)