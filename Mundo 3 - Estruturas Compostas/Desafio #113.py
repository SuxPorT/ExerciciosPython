# Reescreva a função leiaInt() que fizemos no Desafio #104, incluindo agora a possibilidade da digitação de
# um número de tipo inválido. Aproveite e crie também uma função leiaFLoat() com a mesma funcionalidade.


def leiaInt(texto):
    while True:
        try:
            valor = int(input(texto))

        except (ValueError, TypeError):
            print("\033[1;31mERRO! Por favor, digite um número inteiro válido.\033[m\n")
            continue

        except KeyboardInterrupt:
            print("\n\033[1;31mUsuário preferiu não digitar esse número.\033[m\n")
            return 0

        else:
            return int(valor)


def leiaFloat(texto):
    while True:

        try:
            valor = float(input(texto))

        except (ValueError, TypeError):
            print("\033[1;31mERRO! Por favor, digite um número real válido.\033[m\n")
            continue

        except KeyboardInterrupt:
            print("\n\033[1;31mUsuário preferiu não digitar esse número.\033[m")
            return 0

        else:
            return float(valor)


numeroInteiro = leiaInt("Digite um número Inteiro: ")
numeroReal = leiaFloat("Digite um número Real: ")
print(f"\nO valor inteiro digitado foi {numeroInteiro} e o real foi {numeroReal}.")
