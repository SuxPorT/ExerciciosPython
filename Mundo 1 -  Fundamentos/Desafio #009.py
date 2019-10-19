# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um número: "))

print("===" * 3, "TABUADA", "===" *3 )
print("\033[1;32m{}\033[m x \033[1;30m1\033[m = \033[1;34m{}\033[m       \033[1;32m{}\033[m x "
      "\033[1;30m6\033[m = \033[1;34m{}\033[m".format(numero, numero * 1, numero, numero * 6))

print("\033[1;32m{}\033[m x \033[1;30m2\033[m = \033[1;34m{}\033[m       \033[1;32m{}\033[m x "
      "\033[1;30m7\033[m = \033[1;34m{}\033[m".format(numero, numero * 2, numero, numero * 7))

print("\033[1;32m{}\033[m x \033[1;30m3\033[m = \033[1;34m{}\033[m       \033[1;32m{}\033[m x "
      "\033[1;30m8\033[m = \033[1;34m{}\033[m".format(numero, numero * 3, numero, numero * 8))

print("\033[1;32m{}\033[m x \033[1;30m4\033[m = \033[1;34m{}\033[m       \033[1;32m{}\033[m x "
      "\033[1;30m9\033[m = \033[1;34m{}\033[m".format(numero, numero * 4, numero, numero * 9))

print("\033[1;32m{}\033[m x \033[1;30m5\033[m = \033[1;34m{}\033[m       \033[1;32m{}\033[m x "
      "\033[1;30m10\033[m = \033[1;34m{}\033[m".format(numero, numero * 5, numero, numero * 10))
