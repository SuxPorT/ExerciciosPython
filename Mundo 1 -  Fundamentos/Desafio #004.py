# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

texto = input("Escreva algo: ")

print("Qual é o tipo primitivo?\033[1;33m", type(texto))
print("\033[mÉ um número?\033[1;33m", texto.isnumeric())
print("\033[mÉ um texo?\033[1;33m", texto.isalpha())
print("\033[mPossui letra(s) ou número(s)?\033[1;33m", texto.isalnum())
print("\033[mTodas as letras estão em maiúsculo?\033[1;33m", texto.isupper())
print("\033[mTodas as letras estão em minúsculo?\033[1;33m", texto.islower())
print("\033[mPossui apenas espaços?\033[1;33m", texto.isspace())
