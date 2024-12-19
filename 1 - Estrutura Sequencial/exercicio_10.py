#Faça um Programa que peça a temperatura em graus Celsius, 
#transforme e mostre em graus Fahrenheit.

celsius = float(input('Insira o valor em Fahrenheit:'))

def celsius_to_fahre(c):
    calc = (c *(9/5)) + 32
    return calc

print('O valor em Farehnheit é:',celsius_to_fahre(celsius)) 