def return_names():
    import sqlite3

    conn = sqlite3.connect('banco.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")

    usuarios = cursor.fetchall()  

    conn.close()
    nomes = [u[1] for u in usuarios]  

    return nomes
def return_senhas():
    import sqlite3

    conn = sqlite3.connect('banco.db')

    cursor = conn.cursor()

    cursor.execute("SELECT senha FROM games")

    senhas = cursor.fetchall()  

    conn.close()
    senha = [u[0] for u in senhas]  
    print(senha)
    return senha