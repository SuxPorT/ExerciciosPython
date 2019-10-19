# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

funcionario = str(input("Nome do funcionário: "))
salario = float(input("Salário do funcionário: "))

aumento = 1.15 * salario

print("O salário de {}, que era de R${:.2f}, passou a ser R${:.2f} devido ao aumento de 15%."
      .format(funcionario, salario, aumento))
