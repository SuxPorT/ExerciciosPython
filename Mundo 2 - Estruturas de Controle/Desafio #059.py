# Crie um programa que leia dois valores e mostre um menu como o ao lado:
# [1] Somar          [4] Novos números
# [2] Multiplicar    [5] Sair do programa
# [3] Maior
# Seu programa deverá realizar a operação solicitada em cada caso.

numero1 = float(input("\033[1;30mPrimeiro valor: "))
numero2 = float(input("Seundo valor: "))

escolha = 0

while escolha != 7:
    print("\033[1;30m===" * 12)
    print("\033[1;33m[1] \033[1;34mSomar"
          "\n\033[1;33m[2] \033[1;34mSubtrair"
          "\n\033[1;33m[3] \033[1;34mMultiplicar"
          "\n\033[1;33m[4] \033[1;34mDividir"
          "\n\033[1;33m[5] \033[1;34mMaior"
          "\n\033[1;33m[6] \033[1;34mNovos números"
          "\n\033[1;33m[7] \033[1;34mSair do programa")
    print("\033[1;30m===" * 12)

    escolha = int(input("OPÇÃO: "))

    print("===" * 12)

    if escolha == 1:
        print("A soma entre {} e {} é {}.".format(numero1, numero2, numero1 + numero2))
    elif escolha == 2:
        print("A diferença entre {} e {} é {}.".format(numero1, numero2, numero1 - numero2))
    elif escolha == 3:
        print("O resultado de {} x {} é {}.".format(numero1, numero2, numero1 * numero2))
    elif escolha == 4:
        print("A divisão entre {} {} é {}.".format(numero1, numero2, numero1 / numero2))
    elif escolha == 5:

        if numero1 > numero2:
            print("Entre {} e {} o maior valor é {}.".format(numero1, numero2, numero1))
        elif numero2 > numero1:
            print("Entre {} e {} o maior valor é {}.".format(numero1, numero2, numero2))
        else:
            print("{} e {} são valores iguais.".format(numero1, numero2))

    elif escolha == 6:
        print("Informe os números novamente.")
        print("===" * 12)

        numero1 = float(input("Primeiro valor: "))
        numero2 = float(input("Seundo valor: "))

    elif escolha == 7:
        print("\033[1;31m {:^35}".format("SAINDO DO PROGRAMA"))
        print("\033[1;30m===" * 12)
    else:
        print("\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE\033[m")
