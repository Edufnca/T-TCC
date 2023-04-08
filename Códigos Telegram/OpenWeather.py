import requests

API_Key = "30ed0a8d5c67edaea06c268bfc39c538"
city = "itatiba" # Cidade definida

#   Requesição do Json
link_request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&lang=pt_br'
request = requests.get(link_request)
weather = request.json()

#   Uso do Json para pegar informações
Temp = weather['main']['temp'] - 273.15
TempC = int(Temp) #transformção em Celsius
Tempo = weather['weather'][0]['description']