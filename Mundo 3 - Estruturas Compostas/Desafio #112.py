# Dentro do pacote utilidadesCeV que criamos no Desafio #111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como uma função input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.

from modulo.utilidadesCeV import moeda
from modulo.utilidadesCeV import dado

preco = dado.leiaDinheiro("Digite o preço: R$")
moeda.resumo(preco, 35, 22)