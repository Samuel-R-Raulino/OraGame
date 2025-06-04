import sqlite3

# Conectar ao banco
conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

# Novo download_id que você quer colocar
personagem_principal = "Princesa-Zelda"

# Nome do jogo que você quer atualizar
nome_jogo = "The Legend of Zelda: Ocarina of Time"

# Comando para atualizar o download_id do jogo
cursor.execute(
    "UPDATE games SET personagem_principal = ? WHERE nome = ?",
    (personagem_principal, nome_jogo)
)

conn.commit()
print("download_id atualizado com sucesso!")

# Verificar se a alteração foi aplicada
cursor.execute("SELECT nome, download_id FROM games WHERE nome = ?", (nome_jogo,))
resultado = cursor.fetchone()
print(f"Jogo: {resultado[0]}, download_id: {resultado[1]}")

conn.close()

