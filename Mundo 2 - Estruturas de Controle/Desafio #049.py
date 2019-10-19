# Refaça o Desafio #009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite um número: "))

print("=" * 8, "TABUADA", "=" * 8)

for valor in range(1, 11):
    print("{} x {} = {}".format(numero, valor, (numero * valor)))
