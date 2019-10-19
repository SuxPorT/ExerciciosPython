def aumentar(valor=0, taxa=0, formatado=False):
    """
    -> Calcula o aumento de um determinado valor,
    retornando o resultado com ou sem formatação.
    :param valor: o valor que se quer reajustar.
    :param taxa: a porcentagem do aumento.
    :param formatado: (opcional) retorna a saída
    formatada.
    :return: o valor reajustado, com ou sem formato.
    """

    resultado = valor + (valor * taxa / 100)
    return resultado if formatado is False else moeda(resultado)


def diminuir(valor=0, taxa=0, formatado=False):
    resultado = valor - (valor * taxa / 100)
    return resultado if formatado is False else moeda(resultado)


def dobro(valor=0, formatado=False):
    resultado = valor * 2
    return resultado if not formatado else moeda(resultado)


def metade(valor=0, formatado=False):
    resultado = valor / 2
    return resultado if not formatado else moeda(resultado)


def moeda(valor=0, simbolo="R$"):
    return f"{simbolo}{valor:.2f}".replace('.', ',')


def resumo(valor=0, aumento=0, reducao=0):
    texto = "RESUMO DO VALOR"
    tamanho = len(texto) + 14

    print('=' * tamanho)
    print(f"{texto:^29}")
    print('=' * tamanho)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"{aumento}% de aumento: \t{aumentar(valor, aumento, True)}")
    print(f"{reducao}% de redução: \t{diminuir(valor, reducao, True)}")
