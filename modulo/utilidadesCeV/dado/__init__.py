def leiaDinheiro(texto):
    valido = False

    while not valido:
            entrada = str(input(texto)).replace(',', '.').strip()

            if entrada.isalpha() or entrada == "":
                print(f"\033[1;31mERRO! \"{entrada}\" é um preço inválido.\033[m\n")
            else:
                valido = True
                return float(entrada)
