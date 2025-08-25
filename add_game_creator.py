import sqlite3

conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO games (nome, adicionado_por)
    VALUES (?, ?)
''', ("Doom", "nulo"))
conn.commit()
print("Usuário inserido com sucesso!")
conn.close()
