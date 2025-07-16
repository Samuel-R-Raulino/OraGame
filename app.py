from flask import Flask, render_template,request,jsonify,redirect,url_for,session
from get_dados import *
import os 
import mercadopago
import sqlite3

app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_supersegura'
ACCESS_TOKEN = "APP_USR-5515393234086824-051409-a798dc3e1af15b38426c01b84b761393-1952959008"
PUBLIC_KEY = "APP_USR-1b3c0147-9080-4743-b327-109084494912"
@app.route("/")
def redirec():
    session["edit"] = ["GABRIEL","Luan"]
    session["game_buy"] = ""
    return redirect(url_for("home"))
@app.route("/cadastro",methods = ["GET","POST"])

@app.route("/addGame",methods=["GET","POST"])
def add_game_page():
    if request.method == "POST":
        nome = request.form.get("Nome")
        preço = request.form.get("Preço")
        descrição = request.form.get("Descrição")
        img1 = request.form.get("IMG1")
        img2 = request.form.get("IMG2")
        img3 = request.form.get("IMG3")
        requisitos = request.form.get("Requisitos")
        classificação = request.form.get("Classificação")
        id = request.form.get("ID de download")
        personagem = request.form.get("Personagem Principal")
        import sqlite3 
        conn = sqlite3.connect("banco_games.db")
        conn.execute("""
        INSERT INTO games (nome,preço,descrição,img1,img2,img3,requisitos,classificação,download_id,personagem_principal) VALUES (?,?,?,?,?,?,?,?,?,?)
        """,(nome,preço,descrição,img1,img2,img3,requisitos,classificação,id,personagem))
        conn.commit()
        conn.close()
    return render_template("add_game.html")

def cadastro():
    if request.method == "POST":
        dados = request.get_json()
        usuario = dados.get("usuario")
        email = dados.get("email")
        senha = dados.get("senha")

        from ADD_USER import add_user 
        add_user(usuario,email,senha,"")
        from games_bc import set_user 
        set_user(usuario,"")
    return render_template("cadastro.html")

@app.route("/home")
def home():
    added = "no"
    session["img_user"] = "img/user.jpg"
    
    if session.get("add",False) == True:
        from games_bc import add_games
        if session.get("botao_foi_clicado",False):
            print("jogo:"+session.get('game', 'Visitante') )
            print(session.get('username', 'Visitante'))
            add_games(session.get('username', 'Visitante'),session.get('game', 'Visitante'))
            added = "yes,yes"
            ##botao_foi_clicado = False
        else:
            added = "yes,no"
            from games_bc import remove_games 
            remove_games(session.get("username","Visitante"),session.get("game","Visitante"))
        session["add"] = False
        valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
        print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")
    else:
        valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)

    img_user = session["img_user"] 
    usuario = session.get('username', 'Visitante') 
    return render_template("home.html", usuario=usuario, img_user=img_user,added=added)
@app.route("/my_games",methods=["GET","POST"])
def my_games():
    
    valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")

    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)

    #img_user = session["img_user"] 
    img_user = session.get('img_user', 'Visitante') 
    usuario = session.get('username', 'Visitante') 
    from get_dados import return_outnames_imgs
    vals = return_outnames_imgs(usuario)
    if request.method=="POST":
        session["game"] = request.form.get("game")
        session["game_buy"] = request.form.get("game")
        
        return redirect(url_for("game"))  # IMPORTANTE: return aqui!
    return render_template("my_games.html",jogos=vals,usuario=usuario,img_user=img_user)
@app.route("/fliperama")
def fliperama():
    usuario = session.get('username', 'Visitante') 
    return render_template("fliperama.html",usuario=usuario)
@app.route("/fliper")
def fliper():
    return render_template("tela_fliperama.html")
@app.route("/dos")
def dos():
    return render_template("dos.html")
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario in return_names() and senha in return_senhas():
            from ADD_USER import add_user 
            add_user(usuario,senha,"")
            session['username'] = usuario
            return redirect(url_for('home'))
        elif usuario not in return_names():
            print("nome errado")
        elif senha not in return_senhas():
            print("senha errada")
    return render_template("login.html")


@app.route("/sobre")
def sobre():
    
    valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")

    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)

    img_user = session.get('img_user', 'Visitante') 
    usuario = session.get('username', 'Visitante') 
    return render_template("sobre.html",usuario=usuario,img_user=img_user)

@app.route("/games",methods=["GET","POST"])
def games():
    
    valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")

    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)

    #img_user = session["img_user"] 
    img_user = session.get('img_user', 'Visitante') 
    usuario = session.get('username', 'Visitante') 
    from get_dados import return_names_imgs
    vals = return_names_imgs()
    print(vals)
    if request.method=="POST":
        session["game"] = request.form.get("game")
        session["game_buy"] = request.form.get("game")
        
        return redirect(url_for("game"))  # IMPORTANTE: return aqui!
    return render_template("games.html",jogos=vals,usuario=usuario,img_user=img_user,contem_https=contem_https)

def contem_https(texto):
    return 'https://' in texto

@app.route('/game', methods=['GET', 'POST'])
def game():
    session["add"] = False
    session['botao_foi_clicado'] = True
    valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")

    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)
    from games_bc import get_games
    if session.get('game', 'Visitante') not in get_games(session.get('username', 'Visitante') ):
        session["button_state"] = "Adquirir"
    else:
        session["button_state"] = "Remover"
    nome = session.get('game', 'Visitante') 
    usuario = session.get('username', 'Visitante') 

    if request.method == 'POST' and usuario !="Visitante":
        if session["button_state"] == "Adquirir":
            session['botao_foi_clicado'] = True
        else:
            session['botao_foi_clicado'] = False
        session["add"] = True
        return redirect(url_for('home'))
    img_user = session.get('img_user', 'Visitante') 
    take = return_dates(nome)
    preço = take[0]
    descrição = take[1]
    
    img1 = take[2]
    img2 = take[3]
    img3 = take[4]
    contem = False
    if not contem_https(img1):
        img1 = "img/"+take[2]
        img2 = "img/"+take[3]
        img3 = "img/"+take[4]
        contem = True
    
    requisitos = take[5]
    classificação = take[6]
    return render_template("game.html",requisitos=requisitos,img3=img3,nome=nome,preço=preço,descrição=descrição,img1=img1,img2=img2,classificação=classificação,usuario=usuario,img_user=img_user,button_state = session['button_state'],user = session.get('game', 'Visitante'),contem=contem,contem_https=contem_https)


@app.route("/user")
def user():
    img_user = session.get('img_user', 'Visitante') 
    usuario = session.get('username', 'Visitante') 
    return render_template("user.html",usuario=usuario,img_user=img_user)
caminho_db = os.path.join(os.path.dirname(__file__), 'banco_games.db')


# Access tokens


# Instâncias dos serviços
mp = mercadopago.SDK(ACCESS_TOKEN)  # Use o ACCESS_TOKEN aqui para poder consultar pagamentos
#boleto_service = BoletoService(ACCESS_TOKEN)
#pix_service = PixService(ACCESS_TOKEN)

# Função para buscar valor do pagamento pelo id
def buscar_valor_pagamento(id_pagamento):
    try:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        cursor.execute("SELECT preço FROM games WHERE nome = ?", (session["game_buy"],))
        print(session["game_buy"])
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            return 0.1  # Altere se quiser usar o valor real: resultado[0]
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar valor: {e}")
        return None

# Rotas de páginas
@app.route("/cartão")
def index():
    return render_template("cartao.html")

@app.route("/boleto")
def boleto():
    return render_template("boleto.html")

@app.route("/pix")
def pix():
    return render_template("pix.html")
@app.route('/Download')
def Download():
    from get_dados import return_id 
    
    a = session["game_buy"]
    print(a)
    download_id = return_id(a)
    link = f"https://drive.google.com/uc?export=download&id={download_id}"
    print(link)
    return redirect(link)
# Rota API para processar boleto
@app.route("/process_boleto", methods=["POST"])
def process_boleto():
    data = request.json
    id_pagamento = data.get("id_pagamento")
    amount = buscar_valor_pagamento(id_pagamento)

    if amount is None:
        return jsonify({"status": "error", "message": "ID de pagamento inválido"}), 400

    try:
        boleto = boleto_service.criar_boleto(
            amount=amount,
            payer_info={
                "email": data["payer"]["email"],
                "first_name": data["payer"]["first_name"],
                "last_name": data["payer"]["last_name"],
                "cpf": data["payer"]["identification"]["number"],
            }
        )

        if boleto["status"] == "pending":
            return jsonify({
                "status": "success",
                "boleto_url": boleto["transaction_details"]["external_resource_url"],
                "barcode": boleto["transaction_details"]["barcode"],
            })
        else:
            return jsonify({"status": "error"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

from pix import *
# Rota API para gerar o pagamento PIX
@app.route("/pix", methods=["POST"])
def gerar_pix():
    pix_service = PixService(app.secret_key)
    data = request.json
    id_pagamento = data.get("id_pagamento")
    amount = buscar_valor_pagamento(id_pagamento)

    if amount is None:
        return jsonify({"status": "error", "message": "ID de pagamento inválido"}), 400

    try:
        pagamento = pix_service.criar_pagamento_pix("Produto Exemplo", amount)

        if pagamento["status"] == "pending":
            return jsonify({
                "status": "success",
                "qr_code": pagamento["point_of_interaction"]["transaction_data"]["qr_code"],
                "qr_code_base64": pagamento["point_of_interaction"]["transaction_data"]["qr_code_base64"],
                "pagamento_id": pagamento["id"]
            })
        else:
            return jsonify({"status": "error", "message": "Pagamento não gerado"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 🔍 Nova rota para verificar status de pagamento PIX
@app.route("/verificar_status/<int:pagamento_id>")
def verificar_status(pagamento_id):
    try:
        pagamento = mp.payment().get(pagamento_id)
        status = pagamento["response"]["status"]
        return jsonify({"status": status})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Configura API do Gemini
import google.generativeai as genai
genai.configure(api_key="AIzaSyBjsyOiiFE00gTq1sjhqv_vBoJaetRUCEg")
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat()




@app.route('/ia')
def ia():
    nome = return_person(session["game_buy"])
    username = session.get('username', 'Visitante') 
    if (nome == "Prof rogerinho"):
        intro = f"""Oi, você é {nome}, o especialista de XAMPP e especialista em passar pesquisas pros alunos
        Você trabalha no SENAI, para a turma M2, no Senai de Joinville SC, e você deve falar só sobre XAMPP, 100% do tempo"""
    else:
        intro = f"""Oi, você é {nome}, o especialista retro do universo gamer!
        Fale sobre a lore dos jogos, história do projeto, universo, personagens e desenvolvimento.
        Sua fala inicial deve ser carismática, estilo anos 80/90, agressivo no estilo, mas nunca ofensivo."""
    chat.send_message(intro)
    return render_template('atendente.html', nome=nome,username=username)

@app.route('/perguntar', methods=['POST'])
def perguntar():
    pergunta = request.json['mensagem']
    try:
        resposta = chat.send_message(pergunta)
        return jsonify({'resposta': resposta.text})
    except Exception as e:
        return jsonify({'resposta': f"Erro: {e}"}), 500
    
print("inicializando...")
if __name__ == "__main__":
    app.run(debug=True)
