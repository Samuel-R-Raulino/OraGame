import sqlite3


conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM games WHERE nome = ?",
    ("The Legend of Zelda: Ocarina of Time43",)
)

conn.commit()


conn.close()

