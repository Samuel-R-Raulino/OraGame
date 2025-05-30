from flask import Flask, render_template,request,jsonify,redirect,url_for,session
from get_dados import *

app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_supersegura'
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

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/home")
def home():
    usuario = session.get('username', 'Visitante') 
    return render_template("home.html",usuario=usuario)

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
    return render_template("sobre.html")

@app.route("/user")
def user():
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True)
