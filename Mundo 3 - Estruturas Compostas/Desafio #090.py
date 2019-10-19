# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Média de {aluno['Nome'].capitalize()}: "))

if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"

elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"

else:
    aluno["Situação"] = "Reprovado"

for chave, valor in aluno.items():
    print(f"{chave} é igual a {valor}.")
