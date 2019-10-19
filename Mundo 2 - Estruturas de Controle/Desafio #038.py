# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = float(input("Digite o \033[1;36mprimeiro valor\033[m: "))
numero2 = float(input("Digite o \033[1;33msegundo valor\033[m: "))

print("===" * 18)

if numero1 > numero2:
    print("O \033[1;36mprimeiro valor\033[m é \033[1;34mmaior\033[m.")
elif numero1 == numero2:
    print("Não existe \033[1;35mvalor maior\033[m, os dois são \033[1;34miguais.")
else:
    print("O \033[1;33msegundo valor\033[m é \033[1;34mmaior\033[m.")
