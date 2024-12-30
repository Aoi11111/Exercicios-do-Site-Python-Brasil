#Faça um Programa que peça um número 
#correspondente a um determinado ano e em seguida
#informe se este ano é ou não bissexto.

year = int(input('Digite um ano:\n'))

if year%4 == 0 or year%400 == 0:
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')    