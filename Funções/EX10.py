"""
Gabriel Pontel de Mori - 2025

10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). 
Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa 
usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda 
é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade 
de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter()
recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar
a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.
"""
frase = input("Digite uma frase: ")
frase_tratada = (
    frase.replace(',', ' ')
         .replace('.', ' ')
         .replace('!', ' ')
         .replace('?', ' '))

palavras = frase_tratada.split()

palavras_filtradas = list(filter(lambda p: len(p) >= 5, palavras))
print(palavras_filtradas)