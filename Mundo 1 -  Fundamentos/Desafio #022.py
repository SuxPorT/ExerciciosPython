# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo(sem considerar os espaços).
#  - Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome: "))

tamanho = nome.split()

print("Seu nome em maiúsculas é {}.".format(nome.upper()))
print("Seu nome em minúsculas é {}.".format(nome.lower()))
print("Seu nome tem ao todo {} letras.".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome é {} e ele tem {} letras.".format(tamanho[0], len(tamanho[0])))
