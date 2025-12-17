"""
Gabriel Pontel de Mori - 2025

2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70
"""
def apresentar_tabuada(num: int):
    "A função recebera como parametro um numero inteiro"
    "e fará a tabuada dele do 1 ao 10."
    for i in range(1,11):
        produto = i * num
        print(f'{num} x {i} = {produto}')
    
numero = int(input('Digite um numero inteiro: '))
apresentar_tabuada(numero)