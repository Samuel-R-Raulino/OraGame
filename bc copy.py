import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

# Criar a tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preço INTEGER,
    descrição TEXT NOT NULL,
    img TEXT,
    requisitos TEXT,
    classificação TEXT
)
''')

# Confirmar alterações e fechar conexão
conn.commit()

nome = "Half"
preço = 1.5
descrição = "Jogo bom"
img = "main.png"
requisitos = "8gb ram"
classificação = "18+"
print("Banco de dados criado com sucesso!")
try:
    cursor.execute('''
        INSERT INTO games (nome, preço, descrição, img, requisitos, classificação)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, preço, descrição, img, requisitos, classificação))

    conn.commit()
    print("Usuário inserido com sucesso!")

except sqlite3.IntegrityError as e:
    print(f"Erro ao inserir usuário: {e}")
conn.close()