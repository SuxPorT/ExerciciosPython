# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import sample

jogos = []

print("===" * 12)
print("{:^35}".format("JOGO DA MEGA SENA"))
print("===" * 12)

numero = int(input('Número de jogos para sortear: '))

print(f"========= Sorteando {numero} JOGOS =========")

sleep(1)

for palpites in range(1, numero + 1):
    jogos.append(sample(range(1, 61), k=6))

    for rodada, jogo in enumerate(jogos):
        jogo.sort()

    print(f"Jogo {rodada + 1}: {jogo}")

    sleep(1)

print(f"========== < BOA SORTE ! > ==========")
