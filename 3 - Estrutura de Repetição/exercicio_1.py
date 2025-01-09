#Faça um programa que peça uma nota, entre zero e 
#dez. Mostre uma mensagem caso o valor seja 
#inválido e continue pedindo até que o usuário 
#informe um valor válido.

while True:
    num = int(input('\nInsira um número de 1 à 10:\n'))
    
    if num <= 0 or num > 10:
        print('Número inválido, tente de novo.') 
    elif num > 0 and num <= 10:
        break
    
