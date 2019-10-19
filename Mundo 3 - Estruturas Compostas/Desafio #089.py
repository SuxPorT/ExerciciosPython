# Crie um programa que leia o nome de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
lista = []
aluno = 0

while True:
    boletim.append(str(input("Nome: ")).lower())
    aluno += 1

    for vez in range(1, 3):
        boletim.append(float(input(f"Nota {vez}: ")))

    lista.append(boletim[:])
    boletim.clear()

    escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    if escolha not in 'S':
        break
    else:
        print("===" * 8)

print("===" * 10)
print("N° {:>7} {:>14}".format("NOME", "MÉDIA"))
print("---" * 9)

for numero in range(0, aluno):
    print(f"{numero:<4} {lista[numero][0].capitalize():<10} {(lista[numero][1] + lista[numero][2]) / 2:>8}")

print("---" * 9)

while True:
    procura = str(input("Mostrar notas de qual aluno? (999 interrompe): ")).lower()

    if procura == "999":
        print("---" * 9)
        break

    for pessoa in lista:
        for nome in pessoa:
            if procura == nome:
                print(f"Notas de {nome.capitalize()} são {pessoa[1:]}.")

    print("---" * 9)
