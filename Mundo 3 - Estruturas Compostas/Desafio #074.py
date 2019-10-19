# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("===" * 10)
print("Os valores sorteados foram: ", end="")

for valor in numeros:
    print(f"{valor}", end=" ")

print("")
print("===" * 10)
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
