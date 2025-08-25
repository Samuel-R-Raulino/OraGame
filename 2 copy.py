import sqlite3

# Conectar ao banco
conn = sqlite3.connect('banco_games.db')
cursor = conn.cursor()

# Adicionar nova coluna personagem_principal
try:
    cursor.execute("ALTER TABLE games ADD COLUMN adicionado_por TEXT")
    print("Coluna 'adicionado' adicionada com sucesso!")
except sqlite3.OperationalError as e:
    print(f"Erro ao adicionar coluna: {e}")

conn.commit()
conn.close()
