# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from modulo.utilidadesCeV import moeda

preco = float(input("Digite um preço: R$"))

print(f"A metade de {preco} é {moeda.metade(preco)}.")
print(f"O dobro de {preco} é {moeda.dobro(preco)}.")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10)}.")
print(f"Diminuindo 15%, temos {moeda.diminuir(preco, 15)}.")
