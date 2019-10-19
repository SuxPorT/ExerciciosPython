# Refaça o Desafio #051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

a1 = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão da P.A.: "))
termos = int(input("Número de termos: "))

print("===" * 8)

contador = 1

while termos > 0:
    print("{}° termo : {}.".format(contador, a1))

    a1 += razao
    contador += 1
    termos -= 1
