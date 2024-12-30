#Faça um Programa que peça um número e informe 
#se o número é inteiro ou decimal. 

#Dica: utilize uma função de arredondamento.

num = float(input('Insira um número:\n'))

if num == round(num):
    print('É inteiro!')
else:
    print('É decimal!')    
