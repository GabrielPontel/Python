"""
Gabriel Pontel de Mori - 2025

10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares
e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva
o valor em reais do quanto precisará pagar.

Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 
(lê-se pi vezes raio ao quadrado).
"""
from math import pi
from math import pow
raio = float(input('Digite o raio: '))
area = pi * pow(raio,2)
valor = area * 25
print('A area sera de : %.2f e custara: R$%.2f' %(area,valor))