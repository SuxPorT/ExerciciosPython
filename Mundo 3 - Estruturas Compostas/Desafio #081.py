# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    valor = int(input("Digite um valor: "))

    if valor not in lista:
        lista.append(valor)

    print("===" * 30)

    escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if escolha == 'N':
        break

lista.sort(reverse=True)

print("===" * 30)
print(f"Você digitou {len(lista)} valores.")
print(f"Os valores em ordem decrescente são {lista}")

if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")
