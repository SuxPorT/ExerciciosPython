# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo            - Quantas mulheres têm menos de 20 anos
# - Qual é o nome do homem mais velho

numero = soma = velho = homem = mulheres = 0

for pessoa in range(1, 5):
    print("===== {}ª PESSOA =====".format(pessoa))

    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo {M/F]: ")).upper().strip()[0]

    soma += idade
    numero += 1

    if idade > velho and sexo == 'M':
        velho = idade
        homen = nome

    if idade < 20 and sexo == 'F':
        mulheres += 1

print("A média da idade do grupo é {}".format(soma / numero))
print("O homem mais velho tem {} anos e se chama {}".format(velho, homem))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheres))
