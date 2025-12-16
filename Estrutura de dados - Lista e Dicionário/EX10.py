"""
Gabriel Pontel de Mori - 2025

10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista.
Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual 
e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
"""
temperaturas = {'Janeiro': 0, 'Fevereiro':0, 'Marco':0, 'Abril':0, 'Maio':0, 'Junho': 0,
               'Julho':0, 'Agosto':0, 'Setembro':0, 'Outubro':0, 'Novembro':0, 'Dezembro':0}

for chave in temperaturas.keys():
    temperaturas[chave] = int(input(f'Digite a temperatura de {chave}: '))

media_anual = sum(temperaturas.values())/len(temperaturas)

for chave, valor in temperaturas.items():
    if valor > media_anual:
        print(f'O mes de {chave} com a temperatura de {valor}')