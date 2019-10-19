# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pssoas com idade acima da média.

pessoa = dict()
lista = list()
idade = media = 0

while True:
    pessoa.clear()

    pessoa["Nome"] = str(input("Nome: "))

    while True:
        pessoa["Sexo"] = str(input("Sexo: [M/F] ")).upper().strip()[0]

        if pessoa["Sexo"] in "MF":
            break

        print("ERRO! Por favor, digite apenas M ou F.")

    pessoa["Idade"] = int(input("Idade: "))

    lista.append(pessoa.copy())

    while True:
        escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

        if escolha in "SN":
            break

        print("ERRO! Responda apenas S ou N.")

    if escolha == 'N':
        break

print("===" * 15)
print(lista)

print(f"A) Foram cadastradas {len(pessoa)} pessoas.")

for individuo in lista:
    idade += individuo["Idade"]

media = idade / len(pessoa)

print(f"B) A média da idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram: ", end="")

for mulher in lista:
    if mulher["Sexo"] == 'F':
        print(mulher["Nome"], end=" ")

print("")
print("D) Lista de pessoas que estão acima da média: ")

for acima in lista:
    if acima["Idade"] >= media:
        print("         ")

        for chave, valor in acima.items():
            print(f"{chave} = {valor}; ", end="")

        print("")

print("<<< ENCERRADO >>>")
