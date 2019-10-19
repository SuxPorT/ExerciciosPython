# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input("Escreva um número inteiro: "))

print("\033[1m===\033[m" * 10)
print("Escolha a \033[1;34mbase de conversão\033[m:")
print("\033[1m===\033[m" * 10)
print("[\033[1;34m1\033[m] para \033[1;31mbinário\033[m"
      "\n[\033[1;34m2\033[m] para \033[1;31moctal\033[m"
      "\n[\033[1;34m3\033[m] para \033[1;31mhexadecimal\033[m")
print("\033[1m===\033[m" * 10)

escolha = int(input("ESCOLHA: "))
print('\033[1m===\033[m'*10)

if escolha == 1:
    print("{} convertido para \033[1;31mBINÁRIO\033[m é igual a \033[1;32m{}."
          .format(numero, bin(numero)[2:]))
elif escolha == 2:
    print("{} convertido para \033[1;31mOCTAL\033[m é igual a \033[1;32m{}."
          .format(numero, oct(numero)[2:]))
elif escolha == 3:
    print("{} convertido para \033[1;31mHEXADECIMAL\033[m é igual a \033[1;32m{}."
          .format(numero, hex(numero)[2:]))
else:
    print("\033[1;31mERRO! ESCOLHA INVÁLIDA!")
