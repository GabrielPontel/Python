"""
Gabriel Pontel de Mori - 2025

7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
O texto exibido ao fim deve ser parecido com:

"Nome completo: Ana Silva"
"""
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
nomes_completos = list(map(lambda x, y: x.title()+" "+y.title(), nomes,sobrenomes))
print(nomes_completos)