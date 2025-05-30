import mercadopago

class BoletoService:
    def __init__(self, access_token):
        self.sdk = mercadopago.SDK("TEST-5515393234086824-051409-1695a9b4f20262193c59fe82a5de8333-1952959008")

    def criar_boleto(self, amount, payer_info):
        payment_data = {
            "transaction_amount": amount,
            "payment_method_id": "bolbradesco",
            "payer": {
                "email": payer_info["email"],
                "first_name": payer_info["first_name"],
                "last_name": payer_info["last_name"],
                "identification": {
                    "type": "CPF",
                    "number": payer_info["cpf"]
                }
            }
        }

        payment_response = self.sdk.payment().create(payment_data)

        if payment_response["status"] >= 400:
            raise Exception(f"Erro ao criar boleto: {payment_response}")

        return payment_response["response"]
