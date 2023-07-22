from cpf_generator import CPF
import pyodbc

# Conectar ao banco de dados
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=nome_do_servidor;DATABASE=nome_do_banco;UID=nome_de_usuario;PWD=senha')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Consultar os registros com CPF ou N_PIS nulos ou vazios
cursor.execute("SELECT id FROM funcionarios WHERE cpf IS NULL OR cpf = '' OR n_pis IS NULL OR n_pis = ''")

# Gerar CPFs válidos para os registros
for row in cursor.fetchall():
    id = row.id
    cpf = CPF.generate()
    cursor.execute("UPDATE funcionarios SET cpf = ? WHERE id = ?", cpf, id)

# Confirmar as alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

#pip install cpf-generator