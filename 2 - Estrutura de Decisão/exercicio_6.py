#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Insira três números:'))
n2 = float(input())
n3 = float(input())


#Metodo com listas
#def max_num(list_numbers):
#    return max(list_numbers)

#numbers = [n1, n2, n3]
#print(max_num(numbers))

#Metodo pedido pelo exercicio
if n1 > n2 and n1 > n3:
    print('O maior número é:', n1)
elif n2 > n3:
    print('O maior número é:', n2)    
else:
    print('O maior número é:', n3)    