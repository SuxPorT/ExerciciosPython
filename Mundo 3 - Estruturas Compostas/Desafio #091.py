# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {"jogador 1": randint(1, 6),
        "jogador 2": randint(1, 6),
        "jogador 3": randint(1, 6),
        "jogador 4": randint(1, 6),}

print("Valores sorteados:")

for chave, valor in jogo.items():
    print(f"    O {chave} tirou {valor}.")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print("Ranking dos jogadores:")

for indice, valor in enumerate(ranking):
    print(f"    {indice + 1}° lugar: {valor[0]} com {valor[1]}.")
    sleep(1)
