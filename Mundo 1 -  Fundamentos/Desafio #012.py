# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = int(input("Informe o preço do produto: R$"))

preco = 0.95 * produto

print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}."
      .format(produto, preco))
