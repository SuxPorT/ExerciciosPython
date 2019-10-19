# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

divisivel = 0

numero = int(input("Digite um número: "))

for valor in range(1, numero + 1):

    if numero % valor == 0:
        print("\033[1;34m", end=" ")
        divisivel += 1
    else:
        print("\033[1;31m", end=" ")
    print("{}".format(valor), end=" ")

print("\n\033[mO número {} foi divisível {} vezes.".format(numero, divisivel))

if divisivel == 2:
    print("O número {} é PRIMO!".format(numero))
else:
    print("O número {} NÃO É PRIMO!".format(numero))
