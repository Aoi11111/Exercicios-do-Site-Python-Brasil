#Faça um programa que, dado um conjunto de N 
#números, determine o menor valor, o maior valor 
#e a soma dos valores.

list_max = int(input('Insira o máximo de números em sua lista:\n'))
while list_max <0:
    list_max = int(input('Por favor, insira um número válido:\n'))

list_numbers = []

for i in range(list_max):
    num = float(input('Insira um número:\n'))
    list_numbers.append(num)

def list_max_min_sum(list_nums):
    number_max = 0
    number_sum = 0
    
    for i in list_nums:
        number_sum +=i
        
        if i > number_max:
            number_max = i  
    
    number_min = number_max  
    
    for i in list_nums:
        if i < number_min:
            number_min = i    
            
    return number_max, number_min, number_sum

n_max, n_min, n_sum = list_max_min_sum(list_numbers)

print("""
      \nResultado:
      Maior Número - {:.1f}
      Menor Número - {:.1f}
      Soma - {:.1f}
      """.format(n_max, n_min, n_sum))
        