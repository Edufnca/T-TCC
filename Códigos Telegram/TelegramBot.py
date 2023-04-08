from dotenv import load_dotenv
from OpenWeather import *
from Cotações import *
import requests

load_dotenv()


class TelegramBot:
    def __init__(self):
        self.prova=[]
        token = "5943570997:AAGVbVdz88S4KS2SLaJBoTwCsKvTbzVng8g"
        self.url = f"https://api.telegram.org/bot{token}/"


#   Verifica a mensagem do usuário constantemente
    def start(self):
        update_id = None
        while True:
            update = self.get_message(update_id)
            message = update['result']
            if message:
                for message in message:
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        message_txt = message['message']['text']
                        answer_bot = self.answer(message_txt, chat_id, update_id)
                        self.send_answer(chat_id, answer_bot)
                    except:
                        pass


#   Requisição da API do telegram pela Json das mensagens
    def get_message(self, update_id):
        link_request = f"{self.url}getUpdates?timeout=1000"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=1000&offset={update_id + 1}"
        result = requests.get(link_request)
        return json.loads(result.content)


#   Respostas do bot e chamada de funções
    def answer(self, message_txt, chat_id, update_id):
        if message_txt in "oi": #Comandos Cumprimentos
            return "olaaa :D"
        if message_txt in "tempo": # Comandos OpenWeather
            return f"""O tempo em {city} é de {TempC}ºC e {Tempo}"""
        if message_txt in "dolar": # Comandos Cotação
            return f"A Cotação do {QDolar_name} esta em {'%.2f' % QDolar_bid}"

#   Requisição para mandar mensagem pela API
    def send_answer(self, chat_id, answer):
        link_send = f'{self.url}sendMessage?chat_id={chat_id}&text={answer}'
        requests.get(link_send)
        return