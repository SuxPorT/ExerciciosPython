# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - À vista dinheiro/ cheque: 10% de desconto    - Em até 2x no cartão: preço normal
# - À vista no cartão: 5% de desconto            - 3x ou mais no cartão: 20% de juros

from time import sleep

desconto = total = parcela = 0

preco = float(input("Preço do produto: R$"))

print("===" * 10)
print("[\033[1;32m1\033[m] À vista \033[1;34mdinheiro/cheque\033[m: \033[1;33m10%\033[m de desconto."
      "\n[\033[1;32m2\033[m] À vista no \033[1;34mcartão\033[m: \033[1;33m5%\033[m de desconto."
      "\n[\033[1;32m3\033[m] Em até \033[1;34m2x no cartão\033[m: preço normal."
      "\n[\033[1;32m4\033[m] \033[1;34m3x ou mais\033[m no cartão: \033[1;33m20%\033[m de juros.")

condicao = int(input("Condição de pagamento: "))

if condicao == 1:
    desconto = 0.1 * preco
    total = preco - desconto
elif condicao == 2:
    desconto = 0.05 * preco
    total = preco - desconto
elif condicao == 3:
    desconto = 0
    total = preco
elif condicao == 4:
    desconto = str("0.00" + " = Juros de 20%")
    total = preco * 1.2
    parcela = int(input("Número de parcelas: "))
else:
    print("===" * 10)
    print("033[1;31mESCOLHA INVALIDA. COMPRA CANCELADA.\033[m")

print("\033[1;30m===" * 10)
print("{:^32}".format("CALCULANDO..."))
print("===" * 10)

sleep(3)

print("\033[1;37mPREÇO DO PRODUTO\033[m: \033[1;31mR${:.2f}".format(preco))
print("\033[1;37mDESCONTO\033[m: \033[1;36mR${}".format(desconto))

if condicao == 4:
    print("\033[1;37mPREÇO POR PARCELA\033[m: \033[1;31mRS{:.2f}".format(total / parcela))

print("\033[1;37mPREÇO TOTAL A PAGAR\033[m: \033[1;32mR${:.2f}".format(total))
