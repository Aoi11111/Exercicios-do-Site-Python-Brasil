#Faça um programa que peça um número inteiro e 
#determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente 
#por ele mesmo e por 1.

dividers = []
divisors_num = []

num = int(input('Insira um número:'))

for i in range(0, num+1):
   dividers.append(i)
    
for i in range(1, len(dividers)):
    calc = num%dividers[i]
    if calc == 0:
        divisors_num.append(dividers[i])

if len(divisors_num) > 2:
    print('Não é primo')
else:
    print('É primo')    
