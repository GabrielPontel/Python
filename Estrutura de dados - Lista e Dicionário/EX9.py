"""
Gabriel Pontel de Mori - 2025

9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. 
Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi 
igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
"""
correto = ['D','A','C','B','A','D','C','C','A','B']
aluno = []
qtd_questoes = len(correto)
pontuacao = 0

for num in range(0,qtd_questoes):
    resposta = 'laco'
    while(resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D'):
        resposta = input(f'Digite a alternativa assinalada na questao {num+1}: ')
        if (resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D'):
            print("Digite uma alternativa valida!!")
    aluno.append(resposta)

for i in range(0,qtd_questoes):
    if correto[i] == aluno[i]:
        pontuacao+=1
print(f'Nota: {pontuacao}')