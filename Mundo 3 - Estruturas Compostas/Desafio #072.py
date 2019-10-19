# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
# programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
         "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
         "dezoito", "dezenove", "vinte")

while True:

    while True:
        numero = int(input("Digite um número entre 0 e 20: "))

        if 0 <= numero <= 20:
            break

        print("Tente novamente. ", end="")

    print(f"Você digitou o número {tupla[numero]}.")
    print("===" * 10)

    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if escolha in "Nn":
        break

print("===" * 10)
print("ENCERRANDO O PROGRAMA...")
