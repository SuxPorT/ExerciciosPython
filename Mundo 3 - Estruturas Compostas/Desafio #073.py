# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol na ordem de
# colocação. Depois mostre:
# A) Os 5 primeiros time
# B) Os últimos 5 colocados.
# C)Times em ordem alfabética.
# D) Em que posição está o time da Chapecoense.

times = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo",
         "Atlético", "Atlético-PR", "Cruzeiro", "Botafogo", "Santos",
         "Bahia", "Fluminense", "Corinthians", "Chapecoense", "Ceará SC",
         "Vasco da Gama", "Sport Recife", "América-MG", "EC Vitória", "Paraná")

print("===" * 10)
print(f"Lista de times: {times}.")
print("===" * 10)
print(f"Os 5 primeiros times são {times[:5]}.")
print("===" * 10)
print(f"Os 4 últimos são {times[-4:]}.")
print("===" * 10)
print(f"Times em ordem alfabética: {sorted(times)}.")
print("===" * 10)
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")
print("===" * 10)
