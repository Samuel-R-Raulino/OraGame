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


nome = "The Legend of Zelda: Ocarina of Time"
preço = 0.1
descrição = """The Legend of Zelda: Ocarina of Time é um jogo de ação e aventura
lançado em 1998 para o Nintendo 64.
Você joga como Link, um jovem herói destinado a salvar
o reino de Hyrule das forças do mal lideradas por Ganondorf.
Com exploração em mundo aberto, puzzles inteligentes
e viagens no tempo, Ocarina of Time é considerado
um dos melhores e mais influentes jogos de todos os tempos."""
img1 = "Zelda1.png"
img2 = "Zelda2.jpg"
img3 = "Zelda3.jpg"
requisitos = """
Console: Nintendo 64 ou emulador compatível
Armazenamento: Cartucho original ou ROM (~32 MB)
Controles: Controle do N64 ou gamepad configurado no emulador
Sistema: PC com requisitos básicos para emulação (mínimo 1 GHz, 512 MB RAM)
"""
classificação = "Livre"
download_id = "SEU_ID_DO_DRIVE_AQUI"

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