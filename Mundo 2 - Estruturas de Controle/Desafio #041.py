# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM        - Até 25 anos: SÊNIOR
# - ATÉ 14 anos: INFANTIL    - Acima: MASTER
# - Até 19 anos: JUNIOR

from datetime import date

ano = int(input("Informe o ano de seu nascimento: "))

atual = date.today().year
idade = atual - ano

print("\033[1;32m===" * 18)
print("\033[1;32mCONFEDERAÇÃO NACIONAL")
print("\033[1;32m===\033[m" * 18)
print("IDADE: \033[1;33m{} ANOS\033[m".format(idade))

if idade <= 9:
    print("CATEGORIA: \033[1;34mMIRIM")
elif idade <= 14:
    print("CATEGORIA: \033[1;34mINFANTIL")
elif idade <= 19:
    print("CATEGORIA: \033[1;34mJUNIOR")
elif idade <= 25:
    print("CATEGORIA: \033[1;34mSÊNIOR")
else:
    print("CATEGORIA: \033[1;34mMASTER")
