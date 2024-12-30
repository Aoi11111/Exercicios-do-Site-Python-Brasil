#Faça um Programa que peça um número inteiro e 
#determine se ele é par ou impar. 

#Dica: utilize o operador módulo (resto da divisão).

num = float(input('Insira um número:\n'))
rest = int(num%2)

if rest == 1:
    print('É impar')
elif rest == 0:
     print('É par')   