import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect('fliper_games.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela 'usuarios'
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    arquivo TEXT UNIQUE NOT NULL,
    width INTEGER,
    height INTEGER
)
''')

# Confirmar as mudanças
conn.commit()

# Fechar a conexão
conn.close()

print("Tabela criada com sucesso!")
