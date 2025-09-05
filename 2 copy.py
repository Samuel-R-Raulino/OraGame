import sqlite3

# Conectar ao banco
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Adicionar nova coluna personagem_principal
try:
    cursor.execute("ALTER TABLE games ADD COLUMN foto TEXT")
    print("Coluna 'adicionado' adicionada com sucesso!")
except sqlite3.OperationalError as e:
    print(f"Erro ao adicionar coluna: {e}")

conn.commit()
conn.close()
