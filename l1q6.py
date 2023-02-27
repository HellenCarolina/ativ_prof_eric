#importa o valor de pi e a função de potencia (pow)da biblioteca math
from math import pi, pow

#Faça um programa que peça o raio de um circulo, calcule e mostre sua area.
#area do circulo = 2 * pi * r * r
#entrada
raio_do_circulo= float (input('Informe o tamanho do raio do circulo'))

#processamento
area_do_circulo= pi * pow (raio_do_circulo)

#resposta
print(" A area do circulo é{}")
