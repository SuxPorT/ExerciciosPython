# Melhore o jogo do Desafio #028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

computador = randint(0, 10)
total = 0
acerto = False

print("Estou pensando em um número de 0 a 10. Tente adivinhar... ")

sleep(1.5)

print("===" * 20)

escolha = int(input("Terminei! Qual número eu escolhi? "))

print("===" * 20)
print("{:^60}".format("PROCESSANDO..."))
print("===" * 20)

sleep(2)

while not acerto:
    if escolha == computador:
        print("Você acertou! Foram necessários {} palpites".format(total + 1))
        acerto = True
    else:
        total += 1

        if escolha > computador:
            escolha = int(input("Você errou! Tente um número menor: "))

            print('===' * 20)

            sleep(1)

        if escolha < computador:
            escolha = int(input("Você errou! Tente um número maior: "))

            print("===" * 20)

            sleep(1)
