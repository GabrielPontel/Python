"""
Gabriel Pontel de Mori - 2025

14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta.
A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta
e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas
correspondem às espécies de plantas e animais nas áreas, respectivamente.

{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica.
 Dica: use as funções built-in sum() e len().
"""
diversidade = {'Área Norte': [2819, 7236],
               'Área Leste': [1440, 9492],
               'Área Sul': [5969, 7496],
               'Área Oeste': [14446, 49688],
               'Área Centro': [22558, 45148]}
media_plantas = sum(valor[0] for valor in diversidade.values())/len(diversidade)
media_animais = sum(valor[1] for valor in diversidade.values())/len(diversidade)
     
maior = ['Área Norte' , diversidade.get('Área Norte')]
for chave, valor in diversidade.items():
    total = sum(valor)
    if total > sum(maior[1]):
        maior[0] = chave
        maior[1] = valor

print(f'A media de plantas: {media_plantas}') 
print(f'A media de animais: {media_animais}')
print(f'A area com maior diversidade: {maior[0]}')