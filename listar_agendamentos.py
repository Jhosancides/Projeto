import mysql.connector
from conexao import conectar

# Função para listar agendamentos
def listar_agendamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM agendamento")
    resultado = cursor.fetchall()
    print("\n Lista de Agentamentos: ")

    for linha in resultado:
        print(linha)

    cursor.close()
    conexao.close()
    print()
