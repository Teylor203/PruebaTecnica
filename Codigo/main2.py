from os import system
import requests
import sys
import time

def consumo_API_opcion_2(value):
    value = value

    if  __name__ == '__main__':
        url = 'https://api.coinlore.net/api/tickers/'
        response = requests.get(url)

        if response.status_code == 200:
            payloads = response.json()
            data = payloads["data"]
            if data:
                
                for criptomoneda in data:
                    
                    simbolo = criptomoneda["symbol"]
                    name = criptomoneda["name"]
                    price = criptomoneda["price_usd"]
                    price_24 = criptomoneda["percent_change_24h"]
                    rank = criptomoneda["rank"]
                    percent_change_1h = criptomoneda["percent_change_1h"]
                    percent_change_7d = criptomoneda["percent_change_7d"]
                    market_cap_usd = criptomoneda["market_cap_usd"]
                    volume24 = criptomoneda["volume24"]
                    csupply = criptomoneda["csupply"]
                    tsupply = criptomoneda["tsupply"]
                    msupply = criptomoneda["msupply"]

                    if value == 0:
                        print(f"Simbolo: {simbolo} \n Nombre: {name}\n Precio: {price} USD \n Cambio en las ultimas 24 horas: {price_24}% \n \n ")
                    
                    elif value == 1: 
                        print(f"Simbolo: {simbolo} \n Nombre: {name}\n Precio: {price} USD \n Cambio en las ultimas 24 horas: {price_24}% \n Posicion en el mercado: {rank} \n Cambio en los ultimos 7 dias: {percent_change_7d}% \n Cambio en la ultima hora: {percent_change_1h}% \n Capacidad de Mercado: {market_cap_usd} USD \n Suministro Circulante: {csupply} \n Suministro Total: {tsupply} \n Suministro Maximo: {msupply} \n")
            

def consumo_API_opcion_1(value):
    def obtener_informacion_criptomoneda(nombre_criptomoneda):
        url = 'https://api.coinlore.net/api/tickers/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()["data"]
            
            for criptomoneda in data:
                if criptomoneda["name"].lower() == nombre_criptomoneda.lower():
                    return criptomoneda

    def mostrar_informacion_criptomonedas():
        global nombre_criptomoneda_global 
        informacion_criptomoneda = True

        while informacion_criptomoneda:
            time.sleep(1)
            system("cls")
            nombre_busqueda = input("Ingrese el nombre de la criptomoneda: ")
            informacion_criptomoneda = obtener_informacion_criptomoneda(nombre_busqueda)

            if informacion_criptomoneda:
                print(f"Información de {nombre_busqueda.capitalize()}:")
                print("Símbolo:", informacion_criptomoneda["symbol"])
                print("Precio USD:", informacion_criptomoneda["price_usd"])
                print("Cambios en 24h:", informacion_criptomoneda["percent_change_24h"])
                nombre_criptomoneda_global = nombre_busqueda
                informacion_criptomoneda = False
            else:
                print(f"No se encontró información para la criptomoneda {nombre_busqueda}.")
                informacion_criptomoneda = True

    def mostrar_informacion_completa_criptomonedas():
        global nombre_criptomoneda_global
        if nombre_criptomoneda_global:
            criptomoneda = obtener_informacion_criptomoneda(nombre_criptomoneda_global)

            if criptomoneda:
                system("cls")
                simbolo = criptomoneda["symbol"]
                name = criptomoneda["name"]
                price = criptomoneda["price_usd"]
                price_24 = criptomoneda["percent_change_24h"]
                rank = criptomoneda["rank"]
                percent_change_1h = criptomoneda["percent_change_1h"]
                percent_change_7d = criptomoneda["percent_change_7d"]
                market_cap_usd = criptomoneda["market_cap_usd"]
                volume24 = criptomoneda["volume24"]
                csupply = criptomoneda["csupply"]
                tsupply = criptomoneda["tsupply"]
                msupply = criptomoneda["msupply"]

                print(f"Simbolo: {simbolo} \n Nombre: {name}\n Precio: {price} USD \n Cambio en las ultimas 24 horas: {price_24}% \n Posicion en el mercado: {rank} \n Cambio en los ultimos 7 dias: {percent_change_7d}% \n Cambio en la ultima hora: {percent_change_1h}% \n Capacidad de Mercado: {market_cap_usd} USD \n Suministro Circulante: {csupply} \n Suministro Total: {tsupply} \n Suministro Maximo: {msupply} \n")
        else:
            print("No se ha ingresado un nombre de criptomoneda.")

    if value == 0:
        mostrar_informacion_criptomonedas()
    else:
        mostrar_informacion_completa_criptomonedas()

def inicio():
    system("cls")
    bienvenida = "BIENVENIDO A CONSULTOR DE CRIPTOMONEDAS"
    print(61 * "*")
    print(11 * "*" + bienvenida + 11 * "*")
    print(61 * "*")
    print("\n")

    eleccion = "x"
    while not eleccion.isnumeric() or int(eleccion) not in range(1, 4):
        print("""
            [1] - Ver una criptomoneda especifica
            [2] - Ver todas las criptomonedas
            [3] - Salir
            \n""")
        eleccion = input("Elige una opcion:")

    return int(eleccion)


def volver_al_menu():
    system("cls")
    numero = inicio()
    funcion(numero)


def funcion(eleccion):
    eleccion = eleccion

    if eleccion == 1:
        value = 0
        system("cls")
        consumo_API_opcion_1(value)
        print("\n")
        opcion = "p"
        while opcion == "S" or "M":
            opcion = input("Presione [S] para regresar al menu o [M] para mostrar mas informacion de la criptomoneda:")
            if opcion.lower() == "M".lower():
                consumo_API_opcion_1(1)
            elif opcion.lower() == "S".lower():
                n = 4
                volver_al_menu()

    elif eleccion == 2:
        system("cls")
        consumo_API_opcion_2(0)
        opcion = "p"
        while opcion == "s" or "n":
            opcion = input("Presione [S] para regresar al menu o [M] para mostrar mas informacion de todas las criptomonedas:")
            if opcion.lower() == "S".lower():
                n = 4
                volver_al_menu()
            elif opcion.lower() == "M".lower():
                print("\n")
                consumo_API_opcion_2(1)
                
            else:
                print("\n Digite una opcion correctamente")

    elif eleccion == 3:
        sys.exit()
        

        


numero = inicio()
funcion(numero)





