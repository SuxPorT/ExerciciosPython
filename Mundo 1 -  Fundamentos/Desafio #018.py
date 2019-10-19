# Faça um programa um número qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input("Informe um ângulo (°): "))

radiano = radians(angulo)

print("O ângulo de {:.2f}° tem o SENO de {:.2f}."
      "\nO ângulo de {:.2f}° tem o COSSENO de {:.2f}."
      "\nO ângulo de {:.2f}° tem a TANGENTE de {:.2f}."
      .format(angulo, sin(radiano), angulo, cos(radiano), angulo, tan(radiano)))
