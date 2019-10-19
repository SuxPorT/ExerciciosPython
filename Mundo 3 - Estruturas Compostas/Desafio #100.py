# Faça um programa que tenha uma lista chamada sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela
# função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print(f"Sorteando 5 valores da lista: ", end="")

    for numero in range(0, 5):
        valor = randint(1, 10)
        lista.append(valor)

        print(valor, end=" ")

        sleep(0.5)

    print("")

    somaPar(lista)


def somaPar(lista):
    soma = 0

    for par in lista:
        if par % 2 == 0:
            soma += par

    print(f"Somando os valores pares de {lista}, temos {soma}.")


numeros = list()
sorteia(numeros)
