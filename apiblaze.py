import json
import time

import requests


def qualcor(x):
    if int(x) == 1:
        return "V"
    if int(x) == 2:
        return "P"
    if int(x) == 0:
        return "B"
    else:
        return "Error"
# PEGAR DADOS-#


def atualizarlista():
    global lista_de_cores
    while True:

        pegar_dados = requests.get(
            'https://blaze.com/api/roulette_games/recent')

        resultado = json.loads(pegar_dados.content)
        lista_de_cores = []
        lista_de_cores = [x['color'] for x in resultado]
        lista_de_cores = [qualcor(x) for x in lista_de_cores]

        lista_de_cores = list(lista_de_cores)
        return (lista_de_cores)

    time.sleep(30)

    if isinstance(lista_de_cores, list):
        for item in lista_de_cores:
            print(item)
    else:
        print("A variável não é uma lista")
