# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27

reais = float(input("Quanto dinheiro você possui? R$"))

dolares = reais / 3.27

print("Com \033[1;32mR${:.2f}\033[m você pode comprar \033[1;33mUS${:.2f}\033[m".format(reais, dolares))
