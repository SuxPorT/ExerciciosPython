# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

soma = contador = media = maior = menor = 0
resposta = 'S'

while resposta == 'S':

    numero = int(input("Digite um valor: "))

    if numero == 1:
        maior = meenor = numero
    else:

        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    contador += 1
    soma += numero

    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    print("===" * 8)

media = soma / contador

print("A média entre os {} valores vale {}.".format(contador, media))
print("O menor valor vale {} e o maior vale {}.".format(menor, maior))
