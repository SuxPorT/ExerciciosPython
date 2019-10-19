# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceram o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print("===" * 10)

numeros = (int(input('Digite o 1° valor: ')),
           int(input('Digite o 2° valor: ')),
           int(input('Digite o 3° valor: ')),
           int(input('Digite o 4° valor: ')))

print("===" * 10)
print(f"Você digitou os valores {numeros}.")
print("===" * 10)

if 9 in numeros:
    print(f"N° de vezes que apareceu o 9: {numeros.count(9)}.")
else:
    print("O número 9 não foi digitado.")

if 3 in numeros:
    print(f"Posição do primeiro 3: {numeros.index(3) + 1}.")
else:
    print("O valor 3 não foi digitado.")

print("Valores pares: ", end="")

for valor in numeros:
    if valor % 2 == 0:
        print(f"{valor}", end=" ")

print("")
print("===" * 10)
