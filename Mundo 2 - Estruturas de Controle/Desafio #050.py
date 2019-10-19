# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0
par = 0

for vez in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        par += 1

print("Você informou {} números pares e a soma foi {}.".format(par, soma))
