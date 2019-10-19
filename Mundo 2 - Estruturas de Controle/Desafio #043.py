# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso    - 30 até 40: Obesidade
# - Entre 18.5 e 25: Peso ideal       - Acima de 40: Obesidade mórbida
# - 25 até 30: Sobrepeso"""

from time import sleep

print("\033[1;37m===" * 10)
print("\033[1;37mCALCULADORA DE IMC")
print("\033[1;37m===\033[m" * 10)

peso = float(input("Informe o seu peso(kg): "))
altura = float(input("Informe a sua altura(m): "))

imc = peso / (altura ** 2)

print("\033[1;37m===" * 10)
print("\033[1mCALCULANDO...")
print("\033[1;37m===\033[m" * 10)

sleep(3)

print("IMC: \033[1;37m{:.1f}\033[m".format(imc))

if imc < 18.5:
    print("SITUAÇÃO: \033[1;36mABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("SITUAÇÃO: \033[1;34mPESO IDEAL")
elif 25 <= imc < 30:
    print("SITUAÇÃO: \033[1;35mSOBREPESO")
elif 30 <= imc < 40:
    print("SITUAÇÃO: \033[1;33mOBESIDADE")
else:
    print("SITUALÇÃO: \033[1;31mOBESIDADE MÓRBIDA")
