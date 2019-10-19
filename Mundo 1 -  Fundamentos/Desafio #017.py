# Faça um prorgama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input("Informe a medida do cateto oposto (m): "))
cateto_adjacente = float(input("Informe a medida do cateto adjacente (m): "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("Com o cateto oposto medindo {:.2f} m e o cateto adjacente {:.2f} m, a hipotenusa vale {:.2f} m."
      .format(cateto_oposto, cateto_adjacente, hipotenusa))
