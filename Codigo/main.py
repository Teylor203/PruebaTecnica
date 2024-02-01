import requests

def obtener_informacion_criptomoneda():
    url = 'https://api.coinlore.net/api/tickers/'
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()["data"]
        
        print(datos)

obtener_informacion_criptomoneda()
