def return_names():
    import sqlite3

    conn = sqlite3.connect('banco.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")

    usuarios = cursor.fetchall()  

    conn.close()
    nomes = [u[1] for u in usuarios]  
    return nomes
def return_names_game():
    import sqlite3

    conn = sqlite3.connect('games_do_usuario.db')

    cursor = conn.cursor()

    cursor.execute("SELECT usuario FROM user_games")

    usuarios = cursor.fetchall()  

    conn.close()
    nomes = [u[0] for u in usuarios]  
    return nomes
def return_names_imgs():
    vals = {}
    import sqlite3

    conn = sqlite3.connect('banco_games.db')
    cursor = conn.cursor()

    cursor.execute("SELECT nome FROM games")
    nomes = cursor.fetchall()  

    cursor.execute("SELECT img1 FROM games")
    imgs = cursor.fetchall()  

    for x, y in enumerate(nomes):
        vals[y[0]] = imgs[x][0]  # pega o valor dentro da tupla

    conn.close()
    return vals
    return nomes
def return_outnames_imgs(user):
    vals = {}
    import sqlite3
    from games_bc import get_games

    nomes = get_games(user)
    conn = sqlite3.connect('banco_games.db')
    cursor = conn.cursor()
    nomes = nomes.split(",")
    for x in nomes:
        if x!="":
            cursor.execute("SELECT img1 FROM games WHERE nome = ?",(x,))
            img = cursor.fetchall() 
            vals[x] = img[0][0]
    conn.close()
    print(vals)
    return vals
#print(return_outnames_imgs())
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
def return_id(nome):
    dates = []
    
    print(nome)
    import sqlite3

    conn = sqlite3.connect('banco_games.db')
    cursor = conn.cursor()

    query = "SELECT download_id FROM games WHERE nome=?"
    

    cursor.execute(query, (nome,))
    id = cursor.fetchall()
    conn.close()
    print(id)
    return id[0][0]
def return_person(nome):
    
    print(nome)
    import sqlite3

    conn = sqlite3.connect('banco_games.db')
    cursor = conn.cursor()

    query = "SELECT personagem_principal FROM games WHERE nome=?"
    

    cursor.execute(query, (nome,))
    id = cursor.fetchall()
    conn.close()
    print(id)
    return id[0][0]
def return_dates(nome):
    dates = []
    import sqlite3

    conn = sqlite3.connect('banco_games.db')
    cursor = conn.cursor()

    queries = [
        "SELECT preço FROM games WHERE nome=?",
        "SELECT descrição FROM games WHERE nome=?",
        "SELECT img1 FROM games WHERE nome=?",
        "SELECT img2 FROM games WHERE nome=?",
        "SELECT img3 FROM games WHERE nome=?",
        "SELECT requisitos FROM games WHERE nome=?",
        "SELECT classificação FROM games WHERE nome=?"
    ]

    for query in queries:
        cursor.execute(query, (nome,))
        val = cursor.fetchall()
        if val:
            dates.append(val[0][0])
        else:
            dates.append(None)  # Or "" or any default value

    conn.close()
    print(dates)
    return dates
