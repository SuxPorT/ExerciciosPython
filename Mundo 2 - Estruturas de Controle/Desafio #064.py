# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

contador = soma = 0

numero = int(input("Digite um valor entre 0 e 998 (999 para parar): "))

while numero != 999:

    soma += numero
    contador += 1

    print("===" * 10)
    numero = int(input("Digite um valor entre 0 e 998 (999 para parar): "))

print("A soma desses {} números é {}.".format(contador, soma))
