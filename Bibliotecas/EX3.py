"""
Gabriel Pontel de Mori - 2025

8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio 
chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 
para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo 
com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
"""
from random import choice
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
salada = []
for i in range(0,3):
    fruta = choice(frutas)
    frutas.remove(fruta)
    salada.append(fruta)
print(salada)