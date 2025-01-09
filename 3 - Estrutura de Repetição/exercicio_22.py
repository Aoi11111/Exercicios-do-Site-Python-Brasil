#Altere o programa de cálculo dos números primos, 
#informando, caso o número não seja primo, 
#por quais número ele é divisível.

dividers = []
divisors_num = []

num = int(input('Insira um número:\n'))

for i in range(0, num+1):
   dividers.append(i)
    
for i in range(1, len(dividers)):
    calc = num%dividers[i]
    if calc == 0:
        divisors_num.append(dividers[i])


if len(divisors_num) > 2:
    print('Não é primo')
    print('\nOs divisores de', num,'são:\n', divisors_num)
else:
    print('É primo') 
    
