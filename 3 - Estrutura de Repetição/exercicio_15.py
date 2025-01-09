#A série de Fibonacci é formada pela seqüência 
#1,1,2,3,5,8,13,21,34,55,... Faça um programa 
#capaz de gerar a série até o n−ésimo termo.

max_num = int(input('Insira até quantos números de Fibonacci você deseja:\n'))

def fibonacci(max):
    list_fibonacci = [1]
    a, b = 0, 1
    if max == 0:
        list_fibonacci = ['Vazio']
        return list_fibonacci
    elif max == 1:
        return list_fibonacci
    elif max == 2:
        list_fibonacci = [1, 1]
        return list_fibonacci
    else:
        for i in range(max):
            a, b = b, b+a
            list_fibonacci.append(b)
        
        return list_fibonacci  
    
list_fibonacci = fibonacci(max_num)
print(list_fibonacci)      
            
            