# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

numero1 = int(input("Digite a primeira nota: "))
numero2 = int(input("Digite a segunda nota: "))

media = (numero1 + numero2) / 2

print("A média entre \033[1;32m{}\033[m e \033[1;32m{}\033[m é \033[1;33m{}\033[m."
      .format(numero1, numero2, media))
