# Refaça o Desafio #035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print("\033[1;32m===\033[m" * 8)
print("\033[1;32mANALISADOR DE TRIÂNGULOS\033[m")
print("\033[1;32m===\033[m" * 8)

reta1 = float(input("Primeiro segmento: "))
reta2 = float(input("Segundo segmeto: "))
reta3 = float(input("Terceiro segmento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima \033[1;36mPODEM FORMAR\033[m um triângulo.", end="")

    if reta1 == reta2 and reta2 == reta3:
        print("\033[1;34mEQUILÁTERO\033[m(todos os lados iguais).")
    elif reta1 != reta2 != reta3 != reta1:
        print("\033[1;34mESCALENO\033[m(todos os lados diferentes).")
    else:
        print("\033[1;34mISÓSCELES\033[m(dois lagos iguais).")

else:
    print("Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m um triângulo.")
