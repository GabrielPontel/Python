"""
Gabriel Pontel de Mori - 2025

6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
    maior nota
    menor nota
    média
    situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
"""
def gerar_relatorio(notas: list)->list:
    "Função recebe por parametro uma lista de notas e retorna outra com maior,menor,media,situacao"
    relatorio = []
    relatorio.append(max(notas))
    relatorio.append(min(notas))
    relatorio.append(sum(notas)/len(notas))
    relatorio.append('Aprovado' if relatorio[2] >= 6 else 'Reprovado')
    return relatorio
notas = [1,5,9,3]
relatorio = gerar_relatorio(notas)
print(f"O(a) estudante obteve uma média de {relatorio[2]}, com a sua maior nota de {relatorio[0]} pontos e a menor nota de {relatorio[1]} pontos e foi {relatorio[3]}"
)