# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

print("Soma de ímpares múltiplos de 3 entre 1 até 500")

soma = 0
multiplos = 0

for numero in range(1, 501, 2):

    if numero % 3 == 0:
        multiplos += 1
        soma += numero

print("A soma de todos os {} valores solicitados é {}.".format(multiplos, soma))
