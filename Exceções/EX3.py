"""
Gabriel Pontel de Mori - 2025

3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função 
deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum 
erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
"""
def converter_para_float(lista:list)->list:
    "Função converte os elementos de uma lista para float"
    try:
        lista = [float(item) for item in lista]
    except Exception as e:
        print(f'{type(e)} {e}')
    else:
       return lista
    finally:
        print('Fim da execução da função')
lista = ['7','8.6','9.0','10a']
lista = converter_para_float(lista)
print(lista)
