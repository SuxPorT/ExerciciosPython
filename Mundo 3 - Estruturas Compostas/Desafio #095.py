# Aprimore o Desafio #093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

jogador = dict()
partidas = list()
sistema = list()

while True:
    jogador.clear()
    partidas.clear()
    jogador["nome"] = str(input("Nome do jogador: ")).capitalize()
    total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for partida in range(0, total):
        partidas.append(int(input(f"    Quantos gols na partida {partida + 1}? ")))

    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    sistema.append(jogador.copy())

    while True:
        escolha = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

        if escolha in "SN":
            break

        print("ERRO! Escolha inválida.")

    if escolha == 'N':
        print("-=-" * 15)
        break

    print("===" * 15)

print(f"cod nome {'gols':>12} {'total':>12}")

for num, pessoa in enumerate(sistema):
    print(f" {num:<2} {pessoa['nome']:<12} {str(pessoa['gols']):<12} {pessoa['total']}")

print("-=-" * 15)

while True:
    dados = int(input("Mostrar dados de qual jogador (999 para parar)? "))

    if dados == 999:
        break

    if dados >= len(sistema):
        print(f"ERRO! Não existe jogador com código {dados}!")
    else:
        print(f" --- LEVANTAMENTO DO JOGADOR {sistema[dados]['nome']} ---")

        for jogo, numero in enumerate(sistema[dados]["gols"]):
            print(f"    No jogo {jogo + 1} fez {numero} gols.")

    print("===" * 15)
