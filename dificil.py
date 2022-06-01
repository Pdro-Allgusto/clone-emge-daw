from math import ceil

def criar_dicionario():
    dic = {}
    cont = 0
    conversao_car = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
    conversao_naipe = ["D", "S", "H", "C"]
    for i in range(0, len(conversao_car)):
        for j in range(0, len(conversao_naipe)):
            dic.update({conversao_car[i] + conversao_naipe[j]: cont})
            cont += 1
    return dic


def dicionario_key(dict):
    lista = []
    for keys in dict:
        lista.append(keys)
    return lista


def maior_manilha(manilha):
    num = dicionario.get(manilha)
    print(num)
    lista = dicionario_key(dicionario)
    for x in range(num, (num + 4) % 39):
        dicionario.update({lista[x]: 40 + x})


dicionario = criar_dicionario()
print(dicionario)


jogada = input().upper()
rodada = jogada[0:1]
manilha = jogada[2:]
maior_manilha(manilha)

dic_jogo = {}
for i in range(0, 4):
    jogador = input().split(" ")
    dic_jogo.update({jogador[0]: jogador[1]})

lista_jogadores = dicionario_key(dic_jogo)
round_ganhador = [0, 0, 0, 0]
maior_carta = 0

for i in range(0, int(rodada)):
    cartas_jogadas = input().upper().split(" ")
    maior_jogador = 0
    for j in range(0, len(cartas_jogadas)):
        try:
            num_carta = int(dicionario.get(cartas_jogadas[j]))
        except:
            num_carta = 0
        if num_carta > maior_carta:
            maior_carta = num_carta
            maior_jogador = j
    round_ganhador[maior_jogador] += 1

ganhador = "*"
cont_ganhador = 0

for x in range(0, 4):
    if round_ganhador[x] == int(dic_jogo.get(lista_jogadores[x])):
        ganhador = lista_jogadores[x]
        cont_ganhador += 1

if 1 < cont_ganhador > 1:
    ganhador = "*"
print(ganhador)