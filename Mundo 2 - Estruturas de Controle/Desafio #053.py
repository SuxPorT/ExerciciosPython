# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print("PALÍNDROMO")

frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]

print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("Temos um PALÍNDROMO!")
else:
    print("A frase digitada NÃO É UM PALÍNDROMO!")
