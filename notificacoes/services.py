from django.conf import settings
import requests


class Whapi:
    def __init__(self):
        self.token_key = settings.TOKEN_KEY_WHAPI
        self.numero_destinatario = settings.NUMERO_DESTINATARIO

        if self.token_key is None or self.numero_destinatario is None:
            print('TOKEN_API_WHAPI ou NUMERO_DESTINATARIO não foi configurado no .env')
            
    
    def enviar_mensagem_texto(self, mensagem: str):

        if not self.token_key:
            return False
        
        url = "https://gate.whapi.cloud/messages/text"

        payload = {
            "to": self.numero_destinatario,
            "body": mensagem
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.token_key}"
        }

        response = requests.post(url, json=payload, headers=headers)

        try:
            response.raise_for_status()
            print(response.text)
        except Exception as e:
            print(f'Erro: {e}')