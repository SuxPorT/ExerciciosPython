# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


while True:
    numero = int(input("Digite um número (negativo para parar): "))
    print("===" * 12)

    if numero < 0:
        break

    for multiplicador in range(1, 11):

        print(f"{numero} x {multiplicador} = {numero * multiplicador}")

    print("===" * 12)


print("PROGRAMA ENCERRADO.")
