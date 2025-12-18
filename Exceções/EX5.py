"""
Gabriel Pontel de Mori - 2025

5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma 
instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 
estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. 
Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError 
com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será 
realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, 
será exibida uma lista com as notas em cada teste.

Os dados para o teste do código são:

Gabarito da prova:
gabarito = ['D', 'A', 'B', 'C', 'A']

Abaixo temos 2 listas de listas que você pode usar como teste

Notas sem exceção:
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

Notas com exceção:
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] 
not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.
"""
gabarito = ['D', 'A', 'B', 'C', 'A']
testes = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

def valida_alternativas(testes:list):
    for i in range(len(testes)):
        for j in range(len(testes[i])):
            if testes[i][j] not in ['A','B','C','D']:
                raise ValueError(f"A alternativa {testes[i][j]} não é uma opção de alternativa válida")

def calcula_notas(testes:list, gabarito:list)->list:
    resultado = []
    for i in range(len(testes)):
        cont=0
        for j in range(len(testes[i])):
            if testes[i][j] == gabarito[j]:
                cont+=1
        resultado.append(cont) 
    return resultado

try:
    valida_alternativas(testes)
    resultado = calcula_notas(testes,gabarito)
except ValueError as e:
    print(e)
else:
    print(resultado)
