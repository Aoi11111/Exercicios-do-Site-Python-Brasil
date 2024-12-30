#Faça um programa que calcule as raízes de uma 
#equação do segundo grau, na forma ax2 + bx + c. 
#O programa deverá pedir os valores de a, b e c 
#e fazer as consistências, informando ao usuário 
#nas seguintes situações:

#Se o usuário informar o valor de A igual a zero,
#a equação não é do segundo grau e o programa não
#deve fazer pedir os demais valores, sendo 
#encerrado;

#Se o delta calculado for negativo, a equação não
#possui raizes reais. Informe ao usuário e 
#encerre o programa;

#Se o delta calculado for igual a zero a equação 
#possui apenas uma raiz real; informe-a ao usuário;

#Se o delta for positivo, a equação possui duas 
#raiz reais; informe-as ao usuário;
import math

print('Informe os valores de a, b e c respectivamente:')
a = int(input())

if a == 0:
    print('\nNão é uma equação de segundo grau.')
else:
    
    b = int(input())
    c = int(input())
    
    delta = b*b - (4*a*c)

    if delta < 0:
      print('\nNão há raiz real.')  
    elif delta == 0:
        x1 = -b / (2*a)
        print('\nHá uma raiz real: ', x1) 
    elif delta > 0:
        x1 = (-b + math.sqrt(delta) ) / (2*a)
        x2 = (-b  - math.sqrt(delta) ) / (2*a)
        print('\nHá duas raizes reais: {:.1f} e {:.1f}'.format(x1,x2))       