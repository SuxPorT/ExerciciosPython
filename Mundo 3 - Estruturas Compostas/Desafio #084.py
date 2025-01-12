# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] >= maior:
            maior = dados[1]
        if dados[1] <= menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    print("===" * 15)

    escolha = str(input("Quer continuar? [S/N]")).upper().strip()[0]

    print("===" * 15)

    if escolha == 'N':
        break

print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior:.2f}kg. Peso de ", end="")

for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}]", end=" ")

print(f"\nO menor peso foi de {menor:.2f}kg. Peso de ", end="")

for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]", end=" ")
