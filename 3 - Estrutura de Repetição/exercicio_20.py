#Altere o programa de cálculo do fatorial, 
#permitindo ao usuário calcular o fatorial 
#várias vezes e limitando o fatorial a números 
#inteiros positivos e menores que 16.

while True:
    
    num = int(input('Insira um número:\n'))
    while num <= 0 or num > 16:
        num = int(input('Por favor, insira um número positivo, maior que 16:\n'))

    numbers = ''
    numbers_mul = 1

    for i in range(1, num+1):
        numbers+= str(i)
     
        if str(num) not in numbers:
            numbers+='.'
        numbers_mul*=i
  
    print('{}!={}={}'.format(num, numbers, numbers_mul)) 
    
    end = input('Deseja Recomeçar? (s ou n)\n')
    while end not in {'s', 'n'}:
        end = input('Responda com s ou n:\n')
    end.lower
    
    if end == 'n':
        break