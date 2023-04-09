from dotenv import load_dotenv
from OpenWeather import *
from Cotações import *
from Banco_de_dados import *
import requests
import json

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
        if message_txt in 'add prova':
            prova = [] # Lista onde os itens serão salvos
            self.send_answer(chat_id, "Digite o nome que vai dar a Prova:")
            update = self.get_message(update_id)
            message = update['result']
            if message:
                for message in message:
                    message_txt = message['message']['text']
                    while True:
                        if message_txt in prova:
                            break
                        else:
                            prova.append(message_txt)
                            self.send_answer(chat_id, "Salvo!")

            self.send_answer(chat_id, "Coloque a data da prova, exemplo 2023-04-04")
            update = self.get_message(update_id)
            message = update['result']
            if message:
                for message in message:
                    message_txt = message['message']['text']
                    while message_txt == prova[0] or message_txt is None:
                        update = self.get_message(update_id)
                        message = update['result']
                        if message:
                            for message in message:
                                message_txt = message['message']['text']
                        pass
                    if message_txt != prova and message_txt is not None:
                        char = '-/,'
                        dateP = message_txt.translate(str.maketrans('', '', char))
                        prova.append(message_txt)
                        prova.append(dateP)
                        self.send_answer(chat_id, "Salvo!")


            self.send_answer(chat_id, "Coloque uma anotação para a prova")
            update = self.get_message(update_id)
            message = update['result']
            if message:
                for message in message:
                    message_txt = message['message']['text']
                    while message_txt in prova or message_txt is None:
                        update = self.get_message(update_id)
                        message = update['result']
                        if message:
                            for message in message:
                                message_txt = message['message']['text']
                if message_txt != prova and message_txt is not None:
                    prova.append(message_txt)
                    self.send_answer(chat_id, "Salvo!")

            self.send_answer(chat_id, "Confirme as anotações")
            self.send_answer(chat_id, f"{prova}")
            self.send_answer(chat_id, "para Confirmar digite sim ou  nao para cancelar")
            while message_txt != 'sim' or message_txt != 'nao':
                update = self.get_message(update_id)
                message = update['result']
                if message:
                    for message in message:
                        message_txt = message['message']['text']
            self.send_answer(chat_id, "Salvando...")
            self.prova = prova
            if message_txt == 'sim':
                add_prova(f"{prova[0]}", f"{prova[2]}", f"{prova[3]}")
                self.send_answer(chat_id, "A prova foi adcionada com sucesso :D")
            else:
                self.send_answer(chat_id, "Cancelado!")

        if message_txt in 'ver provas':
            read_prova()

#   Requisição para mandar mensagem pela API
    def send_answer(self, chat_id, answer):
        link_send = f'{self.url}sendMessage?chat_id={chat_id}&text={answer}'
        requests.get(link_send)
        return