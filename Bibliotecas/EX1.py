"""
Gabriel Pontel de Mori - 2025

6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio.
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade 
de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para 
ela o número sorteado.
"""
from random import randrange
quantidade=0
while quantidade<1 :
    quantidade = int(input('Digite a quantidade de participantes: '))
    if quantidade<1: 
        print('A quantidade deve ser positiva!!')
sorteado = randrange(1,quantidade)
print(sorteado)