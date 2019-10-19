# Escreva um programa que leia um númreo numero inteiro qualquer e mostre na tela os numero primeiros termos de uma
# Sequência de Fibonacci.
# Ex.: 0 → 1 → 1 → 2 → 3 → 5 → 8

termo = int(input("Número de termos: "))

contador = 3
termo1 = 0
termo2 = 1

print("{} → {}".format(termo1, termo2), end=" ")

while contador <= termo:

    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3

    print(" → {}".format(termo2), end=" ")

    contador += 1
