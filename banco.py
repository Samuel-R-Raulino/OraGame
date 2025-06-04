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
    img1 TEXT,
    img2 TEXT,
    img3 TEXT,
    requisitos TEXT,
    classificação TEXT,
    download_id TEXT
)
''')

# Confirmar alterações e fechar conexão
conn.commit()


nome = "Arcrow"
preço = 0.1
descrição = " game do prof"
img1 = "Arcrow1.png"
img2 = "Arcrow2.jpg"
img3 = "Arcrow3.jpg"
requisitos = """
1gb de ram
"""
classificação = "12+"
download_id = "1abzesPs7qyi3IevB9UFjbMxZHF6ky0B1"

cursor.execute(
    "INSERT INTO games (nome,preço,descrição,img1,img2,img3,requisitos,classificação,download_id) VALUES (?,?,?,?,?,?,?,?,?)",
    (nome,preço,descrição,img1,img2,img3,requisitos,classificação,download_id)
)

conn.commit()


print(f"Dados do jogo atualizados com sucesso!")
    
    # Agora lê os dados inseridos
cursor.execute('SELECT * FROM games')
games = cursor.fetchall()

print("\nJogos no banco:")
for game in games:
    print(game)

conn.close()