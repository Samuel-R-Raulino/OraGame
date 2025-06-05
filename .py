import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

img = ["zelda1.png", "zelda2.png", "zelda3.png"]
# Buscar todos os jogos
cursor.execute('SELECT id, nome FROM games')
games = cursor.fetchall()
nome= "The Legend of Zelda: Ocarina of Time"
cursor.execute('''
UPDATE games
SET img1 = ?, img2 = ?, img3 = ?
WHERE nome = ?
''', (img[0], img[1], img[2], nome))
print(f"Atualizado: {nome} -> {img[0]}, {img[1]}, {img[2]}")

# Salvar alterações e fechar
conn.commit()
conn.close()

print("Imagens atualizadas com sucesso.")
