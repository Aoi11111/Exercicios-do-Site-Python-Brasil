#Faça um Programa que leia um número inteiro 
#menor que 1000 e imprima a quantidade de centenas, 
#dezenas e unidades do mesmo.

num = int(input('Insira um número:\n'))


if num > 1000:
    print('O número não pode ser maior que 1000, tente de novo.')
else:
    num = str(num)
    
    
    if len(num) == 3:
        
        unit = num[2:3]
        ten = num[1:2]
        hundred = num[0:1]
        
        print("""
        Centena: {}
        Dezena: {}
        Unidade: {}
        """.format(hundred, ten, unit))
    elif len(num) == 2:
        
        unit = num[1:2]
        ten = num[0:1]
        
        print("""
        Dezena: {}
        Unidade: {}
        """.format(ten, unit))
    else:
        
        unit = num[0:1]
        print("Unidade:", unit)   
     
             
    
     