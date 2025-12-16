"""
Gabriel Pontel de Mori - 2025

11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. 
Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

Escreva um código que calcule o total de vendas e o produto mais vendido
"""
vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
          'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
maior = ['Produto F', vendas.get('Produto F')]
for chave, valor in vendas.items():
    if valor > maior[1]:
        maior[0] = chave
        maior[1] = valor
total = sum(vendas.values())
print(f'O total de vendas: {total}')
print(f'O produto mais vendido: {maior[0]} com {maior[1]}')