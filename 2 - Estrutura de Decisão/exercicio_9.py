#Faça um Programa que leia três números e 
#mostre-os em ordem decrescente.

n1 = float(input('Insira três números:'))
n2 = float(input())
n3 = float(input())

#Metodo com listas
#numbers = [n1, n2, n3]

#def sort_numbers(list_numbers):
#    list_numbers.sort(reverse=True)
#    return list_numbers

#print(sort_numbers(numbers))

#Metodo pedido pelo exercicio

if n1 > n2 and n1 > n3 and n2 > n3:
    print(n1, n2, n3)
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(n1, n3, n2)
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(n2, n1, n3) 
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(n2, n3, n1)
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(n3, n1, n2)
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(n3, n2, n1)  
                      
    