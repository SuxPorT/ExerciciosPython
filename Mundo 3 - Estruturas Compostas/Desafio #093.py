# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()

jogador["nome"] = str(input("Nome do jogador: ")).capitalize()
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for partida in range(0, total):
    partidas.append(int(input(f"    Quantos gols na partida {partida + 1}? ")))

jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)

print("===" * 10)
print(jogador)
print("===" * 10)

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}.")

print("===" * 10)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")

for indice, valor in enumerate(jogador["gols"]):
    print(f"    => Na partida {indice + 1}, fez {valor} gols.")

print(f"Foi um total de {jogador['total']} gols.")
