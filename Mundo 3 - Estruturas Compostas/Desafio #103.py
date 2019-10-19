# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.


def ficha(jogador='<desconhecido>', numero=0):
    return f"O jogador {jogador} fez {numero} gol(s) no campeonato."


nome = str(input("Nome do jogador: ")).capitalize()
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "":
    print(ficha(numero=gols))
else:
    print(ficha(nome, gols))
