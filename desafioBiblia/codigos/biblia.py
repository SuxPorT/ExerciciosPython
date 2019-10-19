from time import sleep


def buscar():
    while True:
        try:
            arquivo = str(input("Digite o nome do \033[1;32marquivo\033[1;30m a ser indexado: \n>>> "))

            if not arquivo:
                print("\n\033[1;31mFinalizando o programa.\033[1;30m")
                break

            with open(f"{arquivo}.txt", 'r', encoding="utf-8") as texto:
                documento = texto.readlines()
                sleep(1)
                print("\nIndexando... (esse processo pode demorar...)")
                sleep(2)

            texto.close()

            print(f"OK! Foram indexadas \033[1;33m{len(documento)}\033[1;30m linhas")
            sleep(2)
            print("")

            while True:
                palavra = str(input("Digite uma \033[1;32mpalavra\033[1;30m para buscar: \n>>> "))

                if not palavra:
                    print("\n\033[1;31mFinalizando o programa.\033[1;30m")
                    break

                print("\nBuscando...")
                sleep(2)
                print("OK! Encontrei as seguintes linhas:")
                sleep(2)

                for busca in documento:
                    if palavra.lower() in busca.rstrip().lower():
                        if busca[0].isnumeric() or busca[1].isnumeric():
                            busca = busca.replace(busca[0], '-')

                        if busca[1].isnumeric():
                            busca = busca.replace(busca[1], "")

                        print(busca.rstrip())

                print("")

        except FileNotFoundError:
            print("\033[1;31mErro: arquivo não encontrado. Por favor, tente novamente.\033[1;30m\n")
            buscar()

        break


def indexar():
    print('\033[1;30m*' * 30)
    print("********* INDEXADOR **********")
    print('*' * 30, end="\n")

    buscar()
