#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Insira três números:'))
n2 = float(input())
n3 = float(input())

#Metodo com lista
#def max_min(list_numbers):
#    min_num = min(list_numbers)
#    max_num = max(list_numbers)
#    return min_num, max_num

#numbers = [n1, n2, n3]
#min_num, max_num = max_min(numbers)
#print('O menor número é {}, e o maior é {}'.format(min_num, max_num))


#Metodo pedido pelo exercicio

if n1 < n2 and n1 < n3:
    print('O menor número é: ', n1)
elif n2 < n3:
    print('O menor número é: ', n2) 
else:
    print('O menor número é: ', n3) 
       
if n1 > n2 and n1 > n3:
    print('O maior número é:', n1)
elif n2 > n3:
    print('O maior número é:', n2)    
else:
    print('O maior número é:', n3)    

