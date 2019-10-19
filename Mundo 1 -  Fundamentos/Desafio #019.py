# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e  escrevendo o nome do escolhido.

from random import choice

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]

print("O aluno escolhido pelo professor foi {}". format(choice(alunos)))
