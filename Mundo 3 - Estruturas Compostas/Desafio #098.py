# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e
# realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2.
# C) Uma contagem personalizada.

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print("===" * 10)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if fim > inicio:
        while fim >= inicio:
            print(inicio, end=" ")

            sleep(0.5)
            inicio += passo
    else:
        while inicio >= fim:
            print(inicio, end=" ")

            sleep(0.5)
            inicio -= passo

    print("FIM!")
    print("===" * 10, end="\n\n")


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
