#Faça um Programa que peça dois números e imprima a soma.
#precisa de conversão ou os numeros serão entendidos como strings

x = int(input('Insira dois números:'))
y = int(input())

def sum(a, b):
    sum = a+b 
    return sum
    
print('\nA soma dos números é:', sum(x,y))