"""
Gabriel Pontel de Mori - 2025

9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades 
partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 
km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em
cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, 
crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com 
a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta 
de carro.

"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"
"""
viagem = { 'Salvador':[200,850],
           'Fortaleza':[400,800],
           'Natal':[250,300],
           'Aracaju':[300,550]}

def gasto_hotel(qtd_dias: int)->float:
    "Função que ao receber como parametro um inteiro representando a quantidade de dias retorna o valor" 
    "total com hospedagem"
    calculo = 150 * qtd_dias
    return calculo

def gasto_gasolina(viagem:dict, destino:str)->float:
    "Função que ao passar o dicionario com a cidades e suas informações de valores"
    " e a cidade de destino retorna o valor com combustivel do tipo float."
    valores = viagem.get(destino)
    gasto = (valores[1]/14)*5
    return gasto

def gasto_passeio(viagem:dict, destino:str,qtd_dias: int)->float:
    "Função ao passar como parametro o dicionario, destino e a quantidade de dias"
    " da viagem retorna o valor com passeios e alimentação"
    valores = viagem.get(destino)
    gasto = valores[0]*qtd_dias
    return gasto

cidade = input("Digite a cidade de destino: ")
dias = int(input("Digite a quantidade de dias: "))

gastos = gasto_hotel(dias) + gasto_gasolina(viagem,cidade) * 2+ gasto_passeio(viagem,cidade,dias) 
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos,2)} reais")