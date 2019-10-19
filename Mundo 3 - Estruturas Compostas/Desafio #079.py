# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []

while True:
    valor = int(input("Digite um valor: "))

    if valor in lista:
        print("Valor duplicado! Não irei adicionar!")
    else:
        lista.append(valor)

        print("Valor adicionado com sucesso!")

    print("===" * 30)

    escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    print("===" * 30)

    if escolha == 'N':
        break

lista.sort()

print(f"Você digitou os valores {lista}.")
