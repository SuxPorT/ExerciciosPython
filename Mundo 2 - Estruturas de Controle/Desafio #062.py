# Melhore o Desafio #061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

a1 = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão: "))
mais = int(input("Número de termos: "))
print("===" * 8)

an = a1
contador = n = 1
termos = 0

while mais != 0:

    termos += mais

    while contador <= termos:

        print("{}° termo: {}.".format(n, an))
        n += 1
        an += razao
        contador += 1

    print("===" * 8)
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print("===" * 8)
print("Progressão finalizada com {} termos mostrados.".format(termos))
