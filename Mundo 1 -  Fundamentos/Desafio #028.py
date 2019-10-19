# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from random import randint
from time import sleep

numero = randint(0, 5)

print("Estou pensando em um número de 0 a 5. Tente adivinhar... ")
print("-=-" * 20)
escolha = int(input("Terminei! Qual número eu escolhi? "))
print("-=-" * 20)
print("PROCESSANDO...")

sleep(3)

if escolha == numero:
    print("Você acertou!")
else:
    print("Você errou! Escolhi o número {} e não o {}.".format(numero, escolha))
