# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Digite um número: "))

print("Analisando o valor \033[1;32m{}\033[m, seu antecessor é \033[1;31m{}\033[m e seu sucessor é "
      "\033[1;34m{}\033[m.".format(numero, (numero - 1), (numero + 1)))
