#Faça um Programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros 
#quadrados da área a ser pintada. Considere que 
#a cobertura da tinta é de 1 litro para cada 6 
#metros quadrados e que a tinta é vendida em 
#latas de 18 litros, que custam R$ 80,00 ou em 
#galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a 
#serem compradas e os respectivos preços em 3 
#situações:

#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o 
#desperdício de tinta seja menor. 

size_area = float(input('Insira o tamanho da área em metros quadrados:')) 

#Quantidade de litros
liters_of_paint = 0
for i in range(0, int(size_area), 6):
        liters_of_paint+=1

#Apenas as latas        
def cans_calc(l):
    cans, price = 0, 0
    
    while l >= 18:
      l-=18
      cans+=1
    if l < 18:
      cans+=1
      
    for i in range(cans):
        price+=80        
    return cans, price        

#Apenas os galões
def gallons_calc(l):
    gallons, price = 0, 0
    
    while l >= 3.6:
      l-=3.6
      gallons+=1
    if l < 3.6:
      gallons+=1
      
    for i in range(gallons):
        price+=25        
    return gallons, price        

#Galões e Latas
def gallons_cans_calc(l):
    cans, gallons = 0, 0
    price_c, price_g, price = 0, 0, 0
    
    if l > 18:
        while l >= 18:
            l-=18
            cans+=1    
    else:
        while l >= 3.6:
            l-=3.6
            gallons+=1
        
    if l < 3.6:
        gallons+=1   
         
    for i in range(cans):
        price_c+=80
    for i in range(gallons):
        price_g+=25 
    price = price_c+price_g  
             
    return cans, gallons, price

just_cans, just_cans_price = cans_calc(liters_of_paint)
just_gallons, just_gallons_price = gallons_calc(liters_of_paint)
cans, gallons, price = gallons_cans_calc(liters_of_paint)

print('Compra com apenas latas:')
print('- Total de latas: {} \n- R${}\n'.format(just_cans, just_cans_price))
print('Compra com apenas galões:')
print('- Total de galões: {} \n- R${}\n'.format(just_gallons, just_gallons_price))
print('Compra com latas e galões:')
print('- Total de latas: {}\n- Total de galões: {}\n- R${}\n'.format(cans, gallons, price))         

