# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

operadores = []
expressao = str(input("Digite uma expressao: "))

for simbolo in expressao:
    if simbolo == '(':
        operadores.append(simbolo)

    elif simbolo == ')':

        if len(operadores) > 0:
            operadores.pop()
        else:
            operadores.append(')')
            break

if len(operadores) == 0:
    print("Sua expressão está valida!")
else:
    print("Sua expressão está errada!")
