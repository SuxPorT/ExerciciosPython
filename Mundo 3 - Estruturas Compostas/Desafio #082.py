# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
impares = []
pares = []

while True:
    valor = int(input("Digite um valor: "))

    if valor not in lista:
        lista.append(valor)

    print("===" * 30)

    escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if escolha == 'N':
        break

for indice, numero in enumerate(lista):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("===" * 30)
print(f"A lista completa é {lista}.")
print(f"A lista de pares é {pares}.")
print(f"A lista de ímpares é {impares}.")
