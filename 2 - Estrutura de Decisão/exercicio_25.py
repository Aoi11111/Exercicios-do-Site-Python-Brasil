#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação 
#ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que 
#diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

print('Operações Matemáticas.')

num_1 = float(input('Insira dois números:\n'))
num_2 = float(input())

operation = int(input("""
                  Você deseja verificar se seus números são:\n
                  \n1 - par ou ímpar;
                  \n2 - positivo ou negativo;
                  \n3 - inteiro ou decimal.
                  \n"""))
if operation > 3:
    print('Valor inválido, tente novamente.')
else:
    numbers = [num_1, num_2]
    
    if operation == 1:
        for i in numbers:
            
            if i%2 == 0:
                print('\n{} - Par'.format(i))
            else:
                print('\n{} - Impar'.format(i))      
              
    elif operation == 2:
        for i in numbers:
            if i < 0:
               print('\n{} - Negativo'.format(i))
            else:
               print('\n{} - Positivo'.format(i))
            
    else:
        for i in numbers:
            if i == round(i):
               print('\n{} - Inteiro'.format(i))
            else:
               print('\n{} - Decimal'.format(i)) 
                   