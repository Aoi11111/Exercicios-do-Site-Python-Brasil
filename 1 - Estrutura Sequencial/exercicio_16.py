#Faça um programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros 
#quadrados da área a ser pintada. Considere que 
#a cobertura da tinta é de 1 litro para cada 3 
#metros quadrados e que a tinta é vendida em 
#latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de 
#tinta a serem compradas e o preço total.

size_area = float(input('Insira o tamanho da área em metros quadrados:'))

#Quantidade de litros de tinta necessários
liters_of_paint = 0
for i in range(0, int(size_area), 3):
    liters_of_paint+=1
    
#Quantidade de latas
cans=0

while liters_of_paint >= 18:
    liters_of_paint-=18
    cans+=1
      
if liters_of_paint < 18:
    cans+=1   
    
#Preço total 
total_price = 0

for i in range(cans):
    total_price+=80
        
print('- Latas de tinta: {}\n- Preço Total: R${}'.format(cans, total_price))