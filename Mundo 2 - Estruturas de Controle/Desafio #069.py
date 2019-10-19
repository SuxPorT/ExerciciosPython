# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pssoa cadastrada, o programa deverá  perguntar
# se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres te mmenos de 20 anos.

print("===" * 10)
print("CADASTRO DE PESSOAS")

contador = 1
pessoas = homens = mulheres = 0

while True:
    sexo = " "
    escolha = " "

    print("===" * 10)
    print(f"{contador}ª PESSOA")
    print("===" * 10)

    contador += 1

    idade = int(input("Idade: "))

    while sexo not in "MmFf":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    print("===" * 10)

    while escolha not in "SsNn":
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if escolha == 'N':
        print("===" * 10)
        break

if pessoas == 0:
    print("Nenhnuma pessoa tem mais de 18 anos.")
elif pessoas == 1:
    print(f"{pessoas} pessoa tem mais de 18 anos.")
else:
    print(f"{pessoas} pessoas tem mais de 18 anos.")

if homens == 0:
    print("Não foi cadastrado nenhum homem.")
elif homens == 1:
    print(f"Foi cadastrado {homens} homem.")
else:
    print(f"Foram cadastrados {homens} homens.")

if mulheres == 0:
    print("Não há nenhuma mulher com menos de 20 anos.")
elif mulheres == 1:
    print(f"Há {mulheres} mulher com menos de 20 anos.")
else:
    print(f"Há {mulheres} mulheres com menos de 20 anos.")
