# Faça um programa que tenha uma função chamada área(), que receba as dimensões e de um terreno retangular (largura
# e comprimento) e mostre a área do terreno.


def area(largura, comprimento):
    terreno = largura * comprimento

    print(f"A área de um terreno {largura}m x {comprimento}m é de {terreno:.2f}m².")


print("Controle de terreno")
print("===" * 5)

larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))
area(larg, comp)
