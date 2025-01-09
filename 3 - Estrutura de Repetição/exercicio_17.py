#Faça um programa que calcule o fatorial de um 
#número inteiro fornecido pelo usuário. 
#Ex.: 5!=5.4.3.2.1=120

num = int(input('Insira um número:\n'))
while num <= 0:
    num = int(input('Por favor, insira um número válido:\n'))

numbers = ''
numbers_mul = 1
      
for i in range(1, num+1):
    numbers+= str(i)
     
    if str(num) not in numbers:
        numbers+='.'
    numbers_mul*=i
         
print('{}!={}={}'.format(num, numbers, numbers_mul))     