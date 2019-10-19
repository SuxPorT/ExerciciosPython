# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input("Qual é o seu nome? ")

print("É um prazer te conhecer, \033[1;32m{}\033[m!".format(nome))
