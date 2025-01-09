#Faça um programa que leia 5 números e 
#informe o maior número.

numbers = []
max_num = 0
 
for i in range(1, 5):
    num = int(input('Informe um número:\n'))
    numbers.append(num)
    
for i in numbers:
    if i > max_num:
        max_num = i

print('O maior número é:',max_num)         