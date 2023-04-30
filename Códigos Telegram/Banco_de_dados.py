import mysql.connector

#Código que realiza conexão ao banco de dados e suas respectivas funções

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bot_telebot',
)
cursor = conexao.cursor()

# Adicionar Prova - Creat
def add_prova(nome, data, nota):
    comando_add_prova = f'INSERT INTO provas (name_prova, data_prova, notas_prova ) VALUES ("{nome}", {data},"{nota}")'
    cursor.execute(comando_add_prova)
    conexao.commit()
    cursor.close()
    conexao.close()

#Ler todas as provas - Read
def read_prova():
    comando = f'SELECT * FROM provas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado