"""
Gabriel Pontel de Mori - 2025

6) Escreva um programa que peça uma data informando o dia, mês e ano
 e determine se ela é válida para uma análise.
"""
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))
valida = True

if 12<mes or mes<1:
    valida = False

# Meses com 30 dias
if mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        valida = False
elif mes == 2:
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
    if bissexto:
        if dia < 1 or dia>29:
            valida = False
    else:
        if dia<1 or dia>28:
            valida = False
else:
    if dia < 1 or dia > 31:
        valida = False

if valida:
    print("Data Valida!!")
else:
    print("Data Invalida!!")