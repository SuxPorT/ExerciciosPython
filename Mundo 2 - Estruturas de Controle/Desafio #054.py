# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for pessoa in range(1, 8):
    ano = int(input("Informe o ano de nascimento: "))

    idade = date.today().year - ano

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("{} pessoas ainda não atingiram a maioridade, e {} já são de maior.".format(menor, maior))
