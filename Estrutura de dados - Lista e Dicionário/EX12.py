"""
Gabriel Pontel de Mori - 2025

12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. 
A pesquisa foi feita e o votos computados podem ser observados abaixo:

'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
'''

Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, 
informe o design vencedor e a porcentagem de votos recebidos.
"""
votos = {'Design 1' : 1334, 'Design 2' : 982,'Design 3' : 1751,'Design 4' : 210,'Design 5' : 1811}

maior = ['Design 1', votos.get('Design 1')]
for chave, valor in votos.items():
    if valor > maior[1]:
        maior[0] = chave
        maior[1] = valor
print(f'O Vencedor foi o {maior[0]} com {maior[1]} de votos')

total = sum(votos.values())
for chave, valor in votos.items():
    porcentagem = (valor*100)/total
    print('O %s conteve %.2f dos votos' %(chave,porcentagem))