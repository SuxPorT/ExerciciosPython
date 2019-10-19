# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário. Se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcuce e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = dict()
pessoa["Nome"] = str(input("Nome: ")).capitalize()
pessoa["Idade"] = int(input("Ano de nascimento: "))
pessoa["CTPS"] = int(input("Carteira de Trabalho (0 se não tiver): "))

pessoa["Idade"] = datetime.now().year - pessoa["Idade"]

if pessoa["CTPS"] > 0:
    pessoa["Contratação"] = int(input("Ano de contratação: "))
    pessoa["Salário"] = float(input("Salário: R$"))
    pessoa["Aposentadoria"] = pessoa["Idade"] + ((pessoa["Contratação"] + 35) - datetime.now().year)

print("===" * 15)
print(pessoa)

for chave, valor in pessoa.items():
    print(f"{chave} tem o valor {valor}.")
