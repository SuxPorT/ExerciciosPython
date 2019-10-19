# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

comprimento = float(input("Digite o comprimento (m): "))

km = comprimento / 1000
hm = comprimento / 100
dam = comprimento / 10
dm = comprimento * 10
cm = comprimento * 100
mm = comprimento * 1000

print("\033[1;32m{:.2f}\033[m m corresponde a \033[1;33m{:.3f}\033[m km, \033[1;33m{}\033[m hm, "
      "\033[1;33m{}\033[m dam, \033[1;33m{}\033[m dm, \033[1;33m{}\033[m cm e \033[1;33m{}\033[m mm."
      .format(comprimento, km, hm, dam, dm, cm, mm))
