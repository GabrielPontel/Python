"""
Gabriel Pontel de Mori - 2025

3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3.
"""
numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
def triplicar_num(lista: list)->list:
    "A função ao receber como parametro uma lista ela retorna outra lista com seus elementos triplicados."
    return list(map(lambda x:x*3,lista))
mult_3 = triplicar_num(numeros)
print(mult_3)
