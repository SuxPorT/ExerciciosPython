# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIo nas eleições.


def voto(ano):
    from datetime import date

    idade = date.today().year - ano

    print(f"Com {idade} anos: ", end="")

    if idade > 0:
        if 0 < idade < 16:
            return "NÃO VOTA."
        elif 16 <= idade < 18 or idade > 65:
            return "VOTO OPCIONAL."
        else:
            return "VOTO OBRGIATÓRIO."
    else:
        return "IDADE INVÁLIDA."


nascimento = int(input("Em que ano você nasceu? "))
print(voto(nascimento))
