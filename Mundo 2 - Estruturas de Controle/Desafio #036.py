# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

valor = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe o salário do comprador: R$"))
anos = int(input("Informe a quantidade de anos para pagar: "))

prestacao = valor / (anos * 12)

print("\033[1;31m===" * 16)
print("\033[1;36m{:^51}".format("PROCESSANDO..."))
print("\033[1;31m===\033[m" * 16)

sleep(3)

print("Cada parcela irá custar \033[1;32mR${:.2f}\033[m por mês.".format(prestacao))

if prestacao > salario * 0.3:
    print("O empréstimo será negado, pois cada parcela excede mais de \033[1;31m30%\033[m do seu "
          "salário de \033[1;32mR${:.2f}\033[m.".format(salario))
else:
    print("Com o seu salário de \033[1;32mR${:.2f}\033[m, você poderá comprar esta casa!"
          .format(salario))
