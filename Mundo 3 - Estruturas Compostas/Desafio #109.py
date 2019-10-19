# Modifique as funções que foram criadas no Desafio #107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por eles vai ser ou não formatado pela função moeda(), desenvolvida no Desafio #108.

from modulo.utilidadesCeV import moeda

preco = float(input("Digite um preço: R$"))

print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}.")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.")
print(f"Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}.")
print(f"Diminuindo 15%, temos {moeda.diminuir(preco, 15, True)}.")
