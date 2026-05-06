import mysql.connector

from conexao import conectar
from cadastro_agendamento import inserir_agendamento
from listar_agendamentos import listar_agendamentos

conectar()
inserir_agendamento()
listar_agendamentos()

