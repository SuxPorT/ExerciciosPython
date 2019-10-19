# Crie um código que testa se o site Pudim está acessível pelo computador usado.

import urllib.request

try:
    urllib.request.urlopen("http://www.pudim.com.br/")
    print("\n\033[1;32mConsegui acessar o site Pudim com sucesso!")
except:
    print("\n\033[1;31mO site Pudim não está acessível no momento.")
