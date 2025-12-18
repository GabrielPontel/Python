"""
Gabriel Pontel de Mori - 2025

1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses 
números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não 
seja possível de realizar.

Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no 
input para checar os tipos de erro que ocorrem.
"""
try:
    num1 = float(input('Digite o numero1:'))
    num2 = float(input("Digite o numero2:"))
    divisao = num1/num2
except ValueError as e:
    print('Deve ser digitado um float')
except ZeroDivisionError as e2:
    print('Divisao por 0 e impossivel')
else:
    print(f"{num1} / {num2} = {divisao}")
finally:
    print('Conta finalizada')