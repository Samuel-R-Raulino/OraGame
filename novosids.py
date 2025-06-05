
wolf_id = "10a3fKhKPdMw57z9R6NLQEeMI-ERI9ozn"
import sqlite3
conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()



nome = "Wolfenstein 3D"


cursor.execute(
    "UPDATE games SET download_id = ? WHERE nome = ?",
    (wolf_id, nome)
)

conn.commit()
print("dado atualizado com sucesso!")
resultado = cursor.fetchone()

conn.close()
