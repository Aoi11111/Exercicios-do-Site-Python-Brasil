#Faça um Programa que peça dois números e 
#imprima o maior deles.

n1 = float(input('Insira dois números:'))
n2 = float(input())

#Metodo com listas
#numbers = [n1, n2]
#max_num = max(numbers)

#print('O maior número é: ', max_num)

#Metodo pedido pelo exercicio:
if n1 > n2:
    print('O maior número é: ', n1)
else:
    print('O maior número é: ', n2)    