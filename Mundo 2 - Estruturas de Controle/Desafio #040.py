# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem mo final, de acordo
# com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superios: APROVADO

nota1 = float(input("Informe a \033[1mprimeira nota\033[m: "))
nota2 = float(input("Informe a \033[1msegunda nota\033[m: "))

media = (nota1 + nota2) / 2

print("Com as notas \033[1;32m{}\033[m e \033[1;32m{}\033[m, sua média é de \033[1;32m{}."
      .format(nota1, nota2, media))

if media < 5.0:
    print("\033[1;31mSITUAÇÃO: REPROVADO")
elif 5.0 >= media > 7:
    print("\033[1;33mSITUAÇÃO: RECPUERAÇÃO")
else:
    print("\033[1;34mSITUAÇÃO: APROVADO")
