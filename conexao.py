import mysql.connector

# Função para conectar ao banco
def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="oficina"
    )
    print("Conectado")
    return conexao

conectar()