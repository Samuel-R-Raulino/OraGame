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


nome = "Doom II"
preço = 0.1
descrição = " É a sequencia do Doom de 1993, dessa vez, Doom Guy deve enfrentar os demônios em seu planeta natal, a Terra, onde chega de viagem de Marte após os acontecimentos do Doom(1993), e vê o seu coelho de estimação morto pelo demônios, e por isso, ele resolve destruir o exército infernal que agora tentam atormentar sua terra natal. Foi lançado pela ID Software, em 1994, e foi um sucesso superando até mesmo seu antecessor."
img1 = "Arcrow1.png"
img2 = "Arcrow2.jpg"
img3 = "Arcrow3.jpg"
requisitos = """
1gb de ram
"""
classificação = "12+"
download_id = "1ShYoBWisbRqTa5h29BlCOLBvnW3v-6v0"
personagem_principal = ""
cursor.execute(
    "INSERT INTO games (nome,preço,descrição,img1,img2,img3,requisitos,classificação,download_id,personagem_principal) VALUES (?,?,?,?,?,?,?,?,?)",
    (nome,preço,descrição,img1,img2,img3,requisitos,classificação,download_id,personagem_principal)
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