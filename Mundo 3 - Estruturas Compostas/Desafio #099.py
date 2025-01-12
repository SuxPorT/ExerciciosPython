# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(* numeros):
    print("===" * 15)
    print("Analisando os valores passados...")

    if len(numeros) == 0:
        numero = 0
    else:
        numero = numeros[0]

        for valor in numeros:
            if valor >= numero:
                numero = valor

            print(valor, end=" ")

            sleep(0.5)

    print(f"\nForam informados {len(numeros)} valores ao todo.")
    print(f"O maior valor informado foi {numero}.\n")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
