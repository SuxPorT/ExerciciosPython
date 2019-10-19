# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) o maior valor da segunda linha.

matriz = [[], [], []]
pares = coluna3 = linha2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f"Digite um valor para [{linha}, {coluna}]: ")))

print("===" * 15)

linha2 = matriz[1][0]

for linha in range(0, 3):

    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")

        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]

        if coluna == 2:
            coluna3 += matriz[linha][2]

        if matriz[1][coluna] >= linha2:
            linha2 = matriz[1][coluna]

    print("")

print("===" * 15)
print(f"A soma dos valores pares é {pares}.")
print(f"A soma dos valores da terceia coluna é {coluna3}.")
print(f"O maior valor da segunda linha é {linha2}.")
