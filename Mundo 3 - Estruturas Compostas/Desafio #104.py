# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex.: numero = leiaInt("Digite um numero")


def leiaInt(texto):
    while True:
        print(texto, end="")

        valor = input()

        if valor.isnumeric():
            return int(valor)
        else:
            print("\033[1;31mERRO! Digite um número inteiro válido.\033[m\n")


numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}.")
