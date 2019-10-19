# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print("\033[1;33m===" * 10)
print(" " * 4, "CAMPEONATO DE JOKENPÔ")
print("===" * 10)

sleep(1)

print(" " * 8, "\033[1;30mCOMEÇANDO EM")

sleep(1)

print(" " * 13, "3...")

sleep(1)

print(" " * 13, "2...")

sleep(1)

print(" " * 13, "1...\033[m")

sleep(1)

escolha = ["PEDRA", "PAPEL", "TESOURA"]
computador = choice(escolha)

print("\033[1;37m===" * 10)

movimento = str(input("\033[1;37mSeu movimento: ")).upper()

print("Movimento do computador: \033[1;32m{}".format(computador))

sleep(3)

print("\033[1;37m===" * 10)
print("\033[1;33mANALISANDO A SUA DERROTA...")
print("\033[1;37m===\033[m" * 10)

sleep(3)

print("\033[1;34mRESULTADO: {} x {}".format(movimento, computador))

sleep(1)

print("\033[1;37m===" * 10)

sleep(1)

if movimento == "PEDRA" and computador == "PAPEL":
    print("\033[1;31mO COMPUTADOR VENCEU! QUE PENA, TENTE NA PRÓXIMA!")

elif movimento == "PEDRA" and computador == "TESOURA":
    print('\033[1;34mVOCÊ VENCEU! PARABÉNS!')

elif movimento == "PAPEL" and computador == "PEDRA":
    print("\033[1;34mVOCÊ VENCEU! PARABÉNS!")

elif movimento == "PAPEL" and computador == "TESOURA":
    print("\033[1;31mO COMPUTADOR VENCEU! QUE PENA, TENTE NA PRÓXIMA!")

elif movimento == "TESOURA" and computador == "PEDRA":
    print("\033[1;31mO COMPUTADOR VENCEU! QUE PENA, TENTE NA PRÓXIMA!")

elif movimento == "TESOURA" and computador == "PAPEL":
    print("\033[1;34mVOCÊ VENCEU! PARABÉNS!")

elif movimento == computador:
    print("\033[1;36mEMPATE! TENTE OUTRA VEZ!")

elif (movimento != "PEDRA") and (movimento != "PAPEL") and (movimento != "TESOURA"):
    print(" " * 2, "\033[1;31;mERRO: ESCOLHA INEXISTENTE")

    sleep(1)

    print(" " * 2, "\033[1;31;mTERMINANDO O PROGRAMA EM")

    sleep(1)

    print(" " * 13, "3...")

    sleep(1)

    print(" " * 13, "2...")

    sleep(1)

    print(" " * 13, "1...")

    sleep(1)
