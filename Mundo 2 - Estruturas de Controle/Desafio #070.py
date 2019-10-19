# Crie um programa que leia o nome do preço de vários produtos. O programa deverá prguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

gasto = total = contador = custo = 0
barato = " "

while True:
    print("===" * 10)
    nome = str(input("Nome do produto: ")).capitalize()
    preco = float(input("Preço do produto: R$"))

    contador += 1
    gasto += preco

    if preco > 1000:
        total += 1

    if contador == 1 or preco < custo:
        custo = preco
        barato = nome

    escolha = " "

    while escolha not in "SsNn":
        escolha = str(input("Desja continuar? [S/N] ")).strip().upper()[0]

    if escolha == 'N':
        break

print("===" * 10)
print(f"O total gasto na compra foi de R${gasto:.2f}.")

if total == 0:
    print("Nenhum produto custa mais de R$1000.00.")
elif total == 1:
    print("1 produto custa mais de R$1000.00.")
else:
    print(f"{total} produtos custam mais de R$1000.00.")

print(f"{barato} é o produto mais barato, custando R${custo}.")
