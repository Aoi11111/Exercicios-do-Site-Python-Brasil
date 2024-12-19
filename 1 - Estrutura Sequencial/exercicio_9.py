#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)

fahre = float(input('Insira o valor em Fahrenheit'))

def calc(f):
    cels = 5 * ((f-32) / 9)
    return cels

resultado = calc(fahre)
print('Em Celsius é: {:.2f}'.format(resultado))