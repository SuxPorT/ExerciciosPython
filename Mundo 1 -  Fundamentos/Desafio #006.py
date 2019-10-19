# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

numero = int(input("Digite um número: "))

print("O dobro de \033[1;32m{}\033[m é \033[1;33m{}\033[m.".format(numero, (numero * 2)))
print("O triplo de \033[1;32m{}\033[m é \033[1;33m{}\033[m. \nA raiz quadrada de \033[1;32m{}\033[m "
      "é \033[1;33m{:.2f}\033[m.".format(numero, (numero * 3), numero, (pow(numero, (1 / 2)))))
