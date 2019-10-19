# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

primeiro = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão da P.A.: "))

ultimo = primeiro + (10 - 1) * razao
termo = 0

print("===" * 8)

for valor in range(primeiro, (ultimo + 1), razao):
    termo += 1
    print("O {}° termo é {}.".format(termo, primeiro))
    primeiro += razao
