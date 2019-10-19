# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
# simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


def listar():
    print("\033[1;30m====" * 10)
    print(f"{'PESSOAS CADASTRADAS':>29}")
    print("====" * 10)

    with open(file="Desafio #115.txt", mode="r", encoding="utf-8") as arquivo:
        usuarios = str()
        linhas = []

        for linha_dados in arquivo.readlines():
            usuarios += linha_dados

        linha = usuarios.splitlines()

        for nome_idade in linha:
            linhas.append(nome_idade.split(", "))

        for dados in linhas:
            print(f"{dados[0]:<30} {dados[1]}")

    arquivo.close()
    print()


def cadastar():
    print("\033[1;30m====" * 10)
    print(f"{'NOVO CADASTRO':>27}")
    print("====" * 10)

    nome = str(input("Nome: "))

    while True:
        try:
            idade = int(input("\033[1;30mIdade: "))
            texto = f"\n{nome}, {str(idade)} anos"

            with open(file="Desafio #115.txt", mode="a", encoding="utf-8") as arquivo:
                arquivo.write(texto)
            arquivo.close()

            print(f"Novo registro de \033[1;32m{nome}\033[1;30m adicionado.\n")
            break

        except ValueError:
            print("\n\033[1;31mERRO: Por favor, digite um número inteiro válido.\n")


def sair():
    print("\033[1;30m====" * 10)
    print(f"{'Saindo do sistema... Até logo!':>35}")
    print("====" * 10)


while True:
    print("\033[1;30m====" * 10)
    print(f"{'MENU PRINCIPAL':>26}")
    print("====" * 10)
    print("\033[1;32m[1]\033[1;30m \033[1;34m- Ver pessoas cadastradas")
    print("\033[1;32m[2]\033[1;30m \033[1;34m- Cadastrar novas pessoas")
    print("\033[1;32m[3]\033[1;30m \033[1;34m- Sair do Sistema")
    print("\033[1;30m====" * 10)

    try:
        opcao = int(input("\033[1;32mSua opção: "))
        print()

        if opcao == 1:
            listar()
        elif opcao == 2:
            cadastar()
        elif opcao == 3:
            sair()
            break
        else:
            raise ValueError

    except ValueError:
        print("\033[1;31mERRO! Digite uma opção válida!\n")
