# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("\033[1;30mDigite um número: "))

contador = numero
fatorial = 1

print("O fatorial de \033[1;32m{} \033[1;30mé \033[1;34m{}! \033[1;30m= "
      .format(numero, numero), end="")

while contador > 0:
    print("\033[1;32m{}".format(contador), end="")
    print("\033[1;30m x " if contador > 1 else " \033[1;30m= ", end="")
    fatorial *= contador
    contador -= 1

print("\033[1;33m{}".format(fatorial))
