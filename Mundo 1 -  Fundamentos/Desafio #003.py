# Crie um programa que leia dois números e mostre a soma entre eles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print("A soma entre \033[1;32m{}\033[m e \033[1;32m{}\033[m é igual a "
      "\033[1;33m{}\033[m.".format(numero1, numero2, soma))
