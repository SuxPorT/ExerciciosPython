# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome da sua cidade: ")).strip().upper()

print("Sua cidade possui a palavra \"Santo\"? {}".format(cidade[:5] == "SANTO"))
