"""
Gabriel Pontel de Mori - 2025

2) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel 
[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses dados, 
defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
"""
quantidade = 0
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

for gasto in gastos:
    if gasto > 3000:
        quantidade+=1
porcentagem = (quantidade/len(gastos))*100

print(f'Quantidade de gastos acima de R$3000,00: {quantidade}')
print('Em porcentagem representa %.2f' %(porcentagem))