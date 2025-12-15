"""
Gabriel Pontel de Mori - 2025

5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos 
os números primos entre 1 e o número digitado.
"""
primos = []
num_max = int(input("Digite um numero inteiro: "))
for num in range(1,num_max):
    verifica = True
    i = 2
    while(i < num and verifica):
        if(num % i == 0):
            verifica = False
        i+=1
    if(verifica):
        primos.append(num)
print(primos)
