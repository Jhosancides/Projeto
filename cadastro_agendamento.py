import mysql.connector
from conexao import conectar

# Função para inserir agendamento
def inserir_agendamento():
    data_hora = input ("Data e hora do serviço: ")
    motivo = input ("Descreva o motivo: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO agendamento(data_hora, motivo) VALUES (%s, %s)"
    values = (data_hora, motivo)

    cursor.execute(sql, values)
    conexao.commit()

    cursor.close()
    conexao.close()
    print("Agendamento inserido com sucesso!\n")

inserir_agendamento()