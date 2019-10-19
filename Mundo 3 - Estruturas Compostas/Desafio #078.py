# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0

for vez in range(0, 5):
    lista.append(int(input(f"Digite o valor da posição {vez}: ")))

    if vez == 0:
        maior = menor = lista[vez]

    if lista[vez] > maior:
        maior = lista[vez]
    if lista[vez] < menor:
        menor = lista[vez]

print("===" * 10)
print(f"Você digitou os valores {lista}")
print("===" * 10)
print(f"O maior valor digitado foi {maior} nas posições ", end="")

for indice, valor in enumerate(lista):
    if valor == maior:
        print(f"{indice}... ", end="")

print("")
print(f"O menor valor digitado foi {menor} nas posições ", end="")

for indice, valor in enumerate(lista):
    if valor == menor:
        print(f"{indice}... ", end="")

print("")
