"""
Gabriel Pontel de Mori - 2025

2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte
lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
"""
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
lista_terceiro = [tupla[2] for tupla in lista_de_tuplas]
print(lista_terceiro)