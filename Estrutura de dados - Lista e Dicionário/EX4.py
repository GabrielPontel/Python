"""
Gabriel Pontel de Mori - 2025

4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
"""
lista = []
for i in range(0,5):
    lista.append(int(input(f"Digite um numero inteiro para a posicao {i}:")))
for i in range(4,-1,-1):
    print(f'Lista[{i}] = {lista[i]}')