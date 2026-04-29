#importar bliblioteca
#serve para conectar o banco de dados ao python

import mysql.connector

#Executa uma função da lib que realiza a conexão
conexao = mysql.connector.connect(

#Parametros de conexão ao banco de dados
 
    host = "localhost",
    user = "root",
    password = "",
    database = "oficina"
)

print("conectado")

#Função cursor () da lib
#Serve para manipular os dados de envio para o banco
cursor = conexao.cursor()

#Comandos e valores para envio de dados em SQL

sql = "INSERT INTO agendamento(data_hora, motivo) VALUES(%s, %s)"
values = ("2026/04/20", "Teste")


cursor.execute(sql, values)
conexao.commit()


#(criar função)
cursor.execute("SELECT * FROM agendamento")
resultado = cursor.fetchall()


for i in resultado:
    print(i)
#(CRIAR FUNÇÃO)

#(cRIAR MODULARIZAÇÃO)
