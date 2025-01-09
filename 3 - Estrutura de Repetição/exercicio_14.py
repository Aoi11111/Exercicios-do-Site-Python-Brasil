#Faça um programa que peça 10 números inteiros, 
#calcule e mostre a quantidade de números pares 
#e a quantidade de números impares.
list_nums = []
odd = 0
even = 0

for i in range(11):
    num = int(input('Insira um número:\n'))
    list_nums.append(num)

for i in list_nums:
    if i%2 == 1:
        odd +=1
    else:
        even+=1
        
print('Entre os números inseridos, {} são pares e {} são impares.'.format(even, odd))            
    