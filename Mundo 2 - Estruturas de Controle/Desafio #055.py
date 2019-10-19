# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(pessoa)))

    if pessoa == 1:
        maior = peso
        menor = peso

    if peso >= maior:
        maior = peso
    else:
        menor = peso

print("O maior peso foi {:.1f} kg e o menor {:.1f} kg.".format(maior, menor))
