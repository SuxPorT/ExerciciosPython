# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se
# alstar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também
# deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year

print("\033[1;32m===\033[m" * 16)

ano = int(input("Informe o seu ano de nascimento: "))

print("\033[1;32m===\033[m" * 16)

idade = atual - ano

print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, atual))

if idade < 18:
    print("Você ainda não se alistou no serviço imilitar."
          "\nFalta {} anos para se alistar, em {}"
          .format((18 - idade), (atual + 18 - idade)))
elif idade == 18:
    print("É hora de se alistar!")
else:
    print("Você já passou do tempo do alistamento."
          "\nJá se passaram {} anos desde {}"
          .format((idade - 18), (atual + 18 - idade)))
