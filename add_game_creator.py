import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect('noticias.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    imagem1 TEXT,
    imagem2 TEXT,
    imagem3 TEXT,
    descricao TEXT,
    texto TEXT
)
''')

# Confirmar as mudanças
conn.commit()

# Fechar a conexão
conn.close()

print("Tabela criada com sucesso!")
