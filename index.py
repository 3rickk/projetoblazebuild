# IMPORTAÇÕES#
import time

import requests

from apiblaze import atualizarlista

lista_de_cores = []
lista_de_cores = list(atualizarlista())
deve_parar = False

# DEFINIÇÕES #


# Padrões De Cor #
while len(lista_de_cores) < 1:
    time.sleep(0.1)


apostapassada = lista_de_cores[:1]
ultimacor = lista_de_cores[0]
ultimascor = lista_de_cores[0:2]
ultimosnum = lista_de_cores[0:3]
ultimosquatro = lista_de_cores[0:4]


def xadrez(ultimosquatro):
    global aposta
    if ultimosquatro == ["V", "V", "P", "P"]:
        aposta = "P"
        return "=ESTRATÉGIA=\n🟩🟩🟩🟩🟩\nENTRAR NO ⚫️\nproteção ⚪️"
    if ultimosquatro == ["P", "P", "V", "V"]:
        aposta = "V"
        return "=ESTRATÉGIA=\n🟩🟩🟩🟩🟩\nENTRAR NO 🔴\nproteção ⚪️"


def doisseguidos(ultimascor):
    global aposta
    if ultimascor[0] == ultimascor[1]:
        if ultimascor[0] == "V":
            aposta = "P"
            return "=ESTRATÉGIA=\n🟩🟩🟩🟩🟩\nENTRAR NO ⚫️\nproteção ⚪️"
        elif ultimascor[0] == "P":
            aposta = "V"
            return "=ESTRATÉGIA=\n🟩🟩🟩🟩🟩\nENTRAR NO 🔴\nproteção ⚪️"
    else:
        return ""


def padrao(ultimosnum):
    global aposta
    if ultimosnum == ["V", "V", "V"]:
        aposta = "P"
        return "=ESTRATÉGIA=\n🟩🟩🟩🟩🟩\nENTRAR NO ⚫️\nproteção ⚪️"
    if ultimosnum == ["P", "P", "P"]:
        aposta = "V"
        return "=ESTRATÉGIA=\n🟩🟩🟩🟩🟩\nENTRAR NO 🔴\nproteção ⚪️"
    return ""


def sebranco(ultimacor):
    if ultimacor == "B":
        return "BRANCO⚪️⚪️⚪️🎉🎉🎉"
    return ""


resultado_padrao = padrao(ultimosnum)
branco = sebranco(ultimascor)


def vitoria():
    if apostapassada == aposta:
        return "✅✅✅-WIN-✅✅✅"


# MARTIN GALE #


def martingale(ultimacor):
    if ultimacor != apostapassada:
        return """✅✅✅-GALE 1-✅✅✅
"""


def g1(apostapassada):
    martingale(apostapassada)
    if ultimacor == apostapassada:
        return "✅✅✅-WIN-✅✅✅"
    else:
        return "✅✅✅-G1(MARTINGALE)-✅✅✅"


def vp():
    if ultimascor == ["V", "P"]:
        return "Analisando...👾"
    if ultimascor == ["P", "V"]:
        return "Analisando...👾"


def loss():
    if ultimacor != g1 and apostapassada:
        return "LOSS❌"


# API TELEGRAM #


token = "API DO BOT"
cid = "CHAT ID DO BOT"


def mensagem():
    if padrao(ultimosnum):
        mensagem = padrao(ultimosnum)
    if sebranco(ultimascor[0]):
        mensagem = sebranco(ultimascor)
    if xadrez(ultimosquatro):
        mensagem = xadrez()
    if vp():
        mensagem = vp()
    if xadrez(ultimascor):
        mensagem = xadrez(ultimascor)
    if doisseguidos(ultimascor):
        mensagem = doisseguidos(ultimascor)
    if loss():
        mensagem = loss
    elif g1(ultimascor):
        mensagem = g1(ultimascor)
    elif ultimascor[0] != aposta and g1(ultimascor):
        mensagem += "\nLOSS❌"
    elif ultimascor[0] != aposta:
        mensagem += "\nLOSS❌"
    else:
        mensagem = "Analisando..."
    return mensagem


msg = str(mensagem())

url = (
    f"https://api.telegram.org/bot{token}/sendMessage?chat_id={cid}&text={msg}"

)

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Error: {err}")
print(type(ultimascor))
print(mensagem)
print(ultimascor)
