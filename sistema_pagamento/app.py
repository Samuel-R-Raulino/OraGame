from flask import Flask, render_template, request, jsonify
import mercadopago
from boleto import BoletoService
from pix import PixService
import os
import sqlite3

# Caminho e conexão com o banco
caminho_db = os.path.join(os.path.dirname(__file__), 'banco_games.db')

app = Flask(__name__)

# Access tokens
ACCESS_TOKEN = "APP_USR-5515393234086824-051409-a798dc3e1af15b38426c01b84b761393-1952959008"
PUBLIC_KEY = "APP_USR-1b3c0147-9080-4743-b327-109084494912"

# Instâncias dos serviços
mp = mercadopago.SDK(ACCESS_TOKEN)  # Use o ACCESS_TOKEN aqui para poder consultar pagamentos
boleto_service = BoletoService(ACCESS_TOKEN)
pix_service = PixService(ACCESS_TOKEN)

# Função para buscar valor do pagamento pelo id
def buscar_valor_pagamento(id_pagamento):
    try:
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        cursor.execute("SELECT preço FROM games WHERE id = ?", (id_pagamento,))
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

# Rota API para gerar o pagamento PIX
@app.route("/pix", methods=["POST"])
def gerar_pix():
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
