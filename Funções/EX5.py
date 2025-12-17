"""
Gabriel Pontel de Mori - 2025

5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas
de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as)
atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas 
e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

"Nota da manobra: [media]"
"""
def ler_notas()->list:
    "A função faz a leitura de cinco notas e armazena em uma lista que é retornada ao final"
    notas = []
    for i in range(1,6):
        notas.append(float(input(f"Digite a nota {i}: ")))
    return notas

def calcular_media(notas: list)->float:
    "A função calculará a média de um atleta a partir da lista de suas notas"
    notas.remove(max(notas))
    notas.remove(min(notas))
    media = sum(notas)/len(notas)
    return media

notas = ler_notas()
media = calcular_media(notas)
media = round(media,2)
print(f"Nota da manobra: {media}")