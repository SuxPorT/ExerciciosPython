# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = largura * altura

print("Sua parede tem a dimensao de {} m x {} m e sua área mede {} m².".format(largura, altura, area))
print("São necessários {:.2f} L de tinta para pintar essa parede.".format(area / 2))
