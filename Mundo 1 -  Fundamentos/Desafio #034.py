# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumenta é de 15%.

nome = str(input("Nome do funcionário: "))
salario = float(input("Salário do funcionário (R$): "))

if salario > 1250.00:
    print("O novo saláro de {} será R${:.2f}.".format(nome, (salario * 1.10)))
else:
    print("O novo saláro de {} será R${:.2f}.".format(nome, (salario * 1.15)))
