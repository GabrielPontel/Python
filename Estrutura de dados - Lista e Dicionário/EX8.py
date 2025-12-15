"""
Gabriel Pontel de Mori - 2025

8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros 
sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. 
Depois, calcule e mostre a quantidade de produtos doces e amargos.
"""
ids = []
for i in range(0,10):
    ids.append(int(input("Digite o id, sendo ele um numero inteiro: ")))
doces = 0
for i in ids:
    if i%2 == 0:
        doces+=1
amargos = len(ids) - doces
print(f'Quantidade de doces: {doces}')
print(f'Quantidade de amargos: {amargos}')