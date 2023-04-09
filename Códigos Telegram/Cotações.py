import requests

#   Moeda
Moeda = "USD-BRL"
API_Key = f"https://economia.awesomeapi.com.br/last/{Moeda}"

#   Json API
request = requests.get(API_Key)
Quotation = request.json()

#   Informações Json Dólar
QDolar_name = Quotation['USDBRL']['name']
QDolar_bid = float(Quotation['USDBRL']['bid'])
