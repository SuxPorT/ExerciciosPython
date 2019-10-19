# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome
# separadamente.

nome = str(input("Digite o seu nome completo: ")).strip().split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format((nome[0].capitalize())))
print("Seu último nome é {}".format(nome[-1].capitalize()))
