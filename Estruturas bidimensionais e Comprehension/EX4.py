"""
Gabriel Pontel de Mori - 2025

4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro 
elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
"""
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
valores = [tupla[1] for tupla in aluguel if tupla[0] == 'Apartamento']
print(valores)