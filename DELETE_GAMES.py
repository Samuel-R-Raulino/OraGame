import sqlite3


conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM games WHERE id = ?",
    (13,)
)

conn.commit()


conn.close()

