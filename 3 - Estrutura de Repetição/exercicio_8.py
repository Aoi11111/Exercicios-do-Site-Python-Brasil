#Faça um programa que leia 5 números e informe 
#a soma e a média dos números.

numbers = []
max_num = 0
 
for i in range(5):
    num = int(input('Informe um número:\n'))
    numbers.append(num)

sum_num = 0
   
for i in numbers:
    sum_num += i     
    
mean_num = sum_num/len(numbers)    

print('\nA soma dos números fornecidos foi de {} e a média é {}'.format(sum_num, mean_num))