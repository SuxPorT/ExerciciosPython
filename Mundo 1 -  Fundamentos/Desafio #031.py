# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200 Km e R$0.45 para viagens mais longas.

distancia = float(input("Qual a distância da viagem (Km)? "))

if distancia <= 200:
    print("Será cobrado R$0,50 por Km, logo, a viagem irá custar R${:.2f}.".format(distancia * 0.5))
else:
    print("Será cobrado R$0,45 por Km, logo, a viagem irá custar R${:.2f}.".format(distancia * 0.45))
