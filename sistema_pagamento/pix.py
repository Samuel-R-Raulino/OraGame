# pix.py
import mercadopago

class PixService:
    def __init__(self, access_token: str):
        self.sdk = mercadopago.SDK(access_token)

        
    def criar_pagamento_pix(self, titulo: str, valor: float):
        payment_data = {
            "transaction_amount": valor,
            "description": titulo,
            "payment_method_id": "pix",
            "payer": {
                "email": "comprador@email.com",
                "first_name": "João",
                "last_name": "Silva",
                "identification": {
                    "type": "CPF",
                    "number": "12345678909"
                },
                "address": {
                    "zip_code": "06233200",
                    "street_name": "Av. das Nações Unidas",
                    "street_number": "3003",
                    "neighborhood": "Bonfim",
                    "city": "Osasco",
                    "federal_unit": "SP"
                }
            }
        }

        result = self.sdk.payment().create(payment_data)
        print(result["response"])  
        return result["response"]

