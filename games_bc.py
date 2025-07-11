def add_db():
    import sqlite3

    conn = sqlite3.connect('games_do_usuario.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        games TEXT
    )
    ''')
    conn.close()

def set_user(usuario,games):
    import sqlite3

    conn = sqlite3.connect('games_do_usuario.db')
    cursor = conn.cursor()

    cursor.execute('''
            INSERT INTO user_games (usuario, games)
            VALUES (?, ?)
    ''', (usuario, games))
    conn.commit()
    conn.close()
#set_games("GABRIEL","Resident Evil 4, Resident Evil 5, Resident Evil 6")
def get_games(usuario):
    import sqlite3
    conn = sqlite3.connect('games_do_usuario.db')
    cursor = conn.cursor()

    cursor.execute('''
            SELECT games FROM user_games WHERE usuario = ?
    ''', (usuario,))
    valor = cursor.fetchall()
    conn.commit()
    conn.close()

    resultado = valor
    if isinstance(resultado, list):
        if resultado !=[]:
            return resultado[0][0]
        else:
            return ""
    elif isinstance(resultado, tuple):
        if resultado !=():
            return resultado[0][0]
        else:
            return ""
    else:
        return ""

def add_games(usuario, game):
    resultado = get_games(usuario)
    print(resultado)
    if resultado!="":
        jogos_lista = [j.strip() for j in resultado.split(",") if j.strip()]
        if game not in jogos_lista:
            resultado += ","
            resultado += game 

            try:
                import sqlite3
                conn = sqlite3.connect('games_do_usuario.db')
                cursor = conn.cursor()

                cursor.execute(
                    "UPDATE user_games SET games = ? WHERE usuario = ?",
                    (resultado, usuario)
                )
                conn.commit()
                conn.close()
                print(f"[SUCESSO] Jogo '{game}' adicionado para '{usuario}'")
            except Exception as e:
                print(f"[ERRO] ao atualizar o banco de dados: {e}")
        else:
            print("O jogo já foi adicionado")
    else:
        print(resultado)
        if str(resultado):
            resultado += game + ","
        else:
            resultado = game + ","
        try:
            import sqlite3
            conn = sqlite3.connect('games_do_usuario.db')
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE user_games SET games = ? WHERE usuario = ?",
                (resultado, usuario)
            )
            conn.commit()
            conn.close()
            print(f"[SUCESSO] Primeiro jogo '{game}' adicionado para '{usuario}'")
        except Exception as e:
            print(f"[ERRO] ao atualizar o banco de dados: {e}")
