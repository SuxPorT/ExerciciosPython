# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, prgunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("===" * 10)
print("{:^30}".format("CAIXA ELETRÔNICO"))
print("===" * 10)
valor = int(input("Valor a ser sacado: R$"))

total = valor
cedula = 50
numero = 0

while True:
    if total >= cedula:
        total -= cedula
        numero += 1
    else:
        if total > 0:
            print(f"Total de {numero} cédulas de R${cedula}")

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        numero = 0

        if total == 0:
            break

print("===" * 10)
print("Tenha um bom dia e volte sempre!")
