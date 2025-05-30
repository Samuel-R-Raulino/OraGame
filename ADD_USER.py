def add_user(usuario,email,senha,games = ""):
    import sqlite3

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        email INTEGER,
        senha TEXT NOT NULL,
        games TEXT
    )
    ''')
    conn.commit()
    print("Banco de dados criado com sucesso!")
    try:
        cursor.execute('''
            INSERT INTO games (usuario, email, senha,games)
            VALUES (?, ?, ?, ?)
        ''', (usuario, email, senha, games))

        conn.commit()
        print("Usuário inserido com sucesso!")

    except sqlite3.IntegrityError as e:
        print(f"Erro ao inserir usuário: {e}")
    conn.close()
