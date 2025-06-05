import sqlite3


conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()


requisitos = """ 
4gb Ram 
Placa de Video NVIDIA GTX 1650 Super
Processador core I5
Intel Core i5-12400F // AMD Ryzen 5 5600X
"""
nome_jogo = "Arcrow"


cursor.execute(
    "UPDATE games SET requisitos = ? WHERE nome = ?",
    (requisitos, nome_jogo)
)

conn.commit()
print("dado atualizado com sucesso!")
cursor.execute("SELECT nome, download_id FROM games WHERE nome = ?", (nome_jogo,))
resultado = cursor.fetchone()
print(f"Jogo: {resultado[0]}, download_id: {resultado[1]}")

conn.close()

