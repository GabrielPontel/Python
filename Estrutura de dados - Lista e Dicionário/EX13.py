"""
Gabriel Pontel de Mori - 2025

13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente 
a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação
das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma 
lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. 
O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves 
de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as)
colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
"""
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {}
for salario in salarios:
    abono = salario*0.1
    if abono < 200:
        abonos[salario] = 200
    else:
        abonos[salario] = abono

maior = abonos.get(1172)
for valor in abonos.values():
    if valor > maior:
        maior = valor

quantidade_abono_minimo = 0
for abono in abonos.values():
    if abono == 200:
        quantidade_abono_minimo += 1

print(f'O maior valor de abono foi de : {maior}') 
print(f'A quantidade de funcionarios que receberam o abono minimo foi de: {quantidade_abono_minimo}')       