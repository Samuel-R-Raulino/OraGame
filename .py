import sqlite3

conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

# Suponha que você quer deletar o jogo com id = 3
cursor.execute('DELETE FROM games WHERE id = ?', (36,))

conn.commit()
print("Linha deletada com sucesso!")
conn.close()
