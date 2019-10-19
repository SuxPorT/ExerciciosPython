# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número e
# calcule o outro chamado "show", que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(numero, show=False):
    """
    -> Cálcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número jogador.
    """

    resultado = 1

    for valor in range(numero, 0, -1):
        if show:
            print(valor, end="")

            if valor > 1:
                print(end=" x ")
            else:
                print(" = ", end="")

        resultado *= valor

    return resultado


print(fatorial(6, show=True))
