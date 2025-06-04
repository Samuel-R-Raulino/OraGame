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
def redirect():
    return redirect(url_for("home"))
@app.route("/cadastro",methods = ["GET","POST"])


def cadastro():
    if request.method == "POST":
        dados = request.get_json()
        usuario = dados.get("usuario")
        email = dados.get("email")
        senha = dados.get("senha")

        from ADD_USER import add_user 
        add_user(usuario,email,senha,"")
    return render_template("cadastro.html")

@app.route("/home")
def home():
    session["img_user"] = "img/user.jpg"

    valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")

    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)

    img_user = session["img_user"] 
    usuario = session.get('username', 'Visitante') 
    return render_template("home.html", usuario=usuario, img_user=img_user)


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

    img_user = session["img_user"] 
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

    img_user = session["img_user"] 
    usuario = session.get('username', 'Visitante') 
    from get_dados import return_names_imgs
    vals = return_names_imgs()
    print(vals)
    if request.method=="POST":
        session["game"] = request.form.get("game")
        session["game_buy"] = request.form.get("game")
        
        return redirect(url_for("game"))  # IMPORTANTE: return aqui!
    return render_template("games.html",jogos=vals,usuario=usuario,img_user=img_user)

@app.route("/game")
def game():
    
    valor_game_buy = session.get("game_buy", "NÃO DEFINIDO")
    print(f"Valor atual de game_buy na sessão: '{valor_game_buy}'")

    if valor_game_buy == "":
        print("O valor de game_buy está vazio")
    else:
        print("O valor de game_buy NÃO está vazio:", valor_game_buy)

    img_user = session["img_user"] 
    usuario = session.get('username', 'Visitante') 
    nome = session.get('game', 'Visitante') 
    take = return_dates(nome)
    preço = take[0]
    descrição = take[1]

    img1 = "img/"+take[2]
    img2 = "img/"+take[3]
    img3 = "img/"+take[4]
    print(img3)
    requisitos = take[5]
    classificação = take[6]
    return render_template("game.html",requisitos=requisitos,img3=img3,nome=nome,preço=preço,descrição=descrição,img1=img1,img2=img2,classificação=classificação,usuario=usuario,img_user=img_user)


@app.route("/user")
def user():
    img_user = session["img_user"] 
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

print("inicializando...")
if __name__ == "__main__":
    app.run(debug=True)
