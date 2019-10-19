# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que
# ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a velocidade do carro (Km/h?) "))

if velocidade > 80:
    print("MULTADO! Você excedeu o limite de 80 Km/h e deve pagar R$ {:.2f}".format((velocidade - 80) * 7))
else:
    print("Tenha um bom dia! Dirija com segurança!")
