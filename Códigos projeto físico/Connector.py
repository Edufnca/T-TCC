#bibliotecas
import sys
from machine import Pin
from time import sleep

#definições iniciais

#chat_id = ''
#bot_token = ''
#bot_name = ''

def connect():
    wifi_name = " "
    password = " "
    import network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.scan()
    station.connect(wifi_name, password)
    
    if station.isconnected() == True:
        print("conectado")
        return

    while station.isconnected() == False:
        pass
    print('A conexão foi um sucesso!')
    print(station.ifconfig())
    #station.active(False)
