# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

print("===" * 10)
print("PAR OU ÍMPAR")
print("===" * 10)

while True:
    computador = randint(0, 11)
    escolha = " "
    resultado = " "

    numero = int(input("Digite um valor: "))
    print("===" * 10)

    total = computador + numero

    while escolha not in "PpIi":
        escolha = str(input("Par ou ímpar? [P/I] ")).upper().strip()[0]

    print("===" * 10)
    print(f"Você jogou {numero} e o computador {computador}, resultando em {total}",
          "(ÍMPAR)" if total % 2 == 1 else "(PAR)")

    if total % 2 == 0:

        if escolha == 'P':
            resultado = "GANHOU"
            vitorias += 1
        else:
            resultado = "PERDEU"
            break

    elif total % 2 == 1:

        if escolha == 'P':
            resultado = "PERDEU"
            break
        else:
            resultado = "GANHOU"
            vitorias += 1

    print(f"RESULTADO: VOCÊ {resultado}!")
    print("===" * 10)
    print("Vamos jogar novamente...")
    print("===" * 10)

print("===" * 10)
print(f"RESULTADO: VOCÊ {resultado}!")
print("===" * 10)
print(f"GAME OVER! Você ganhou {vitorias} vezes.")
