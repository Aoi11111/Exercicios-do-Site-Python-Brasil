#Uma fruteira está vendendo frutas com a seguinte 
#tabela de preços:

#                   Até 5 Kg                Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o 
#valor total da compra ultrapassar R$ 25,00, receberá
#ainda um desconto de 10% sobre este total. 
#Escreva um algoritmo para ler a quantidade (em Kg) 
#de morangos e a quantidade (em Kg) de maças 
#adquiridas e escreva o valor a ser pago pelo cliente.
from exercicio_27_function import promotion_store

def price_item(price, kg):
    total = 0
    
    for i in range(int(kg)):
        total += price
    return total    
    
apples_kg = float(input('Insira o kilo das maçãs:\n'))
strawberry_kg = float(input('Insira o kilo dos morangos:\n'))

if apples_kg <= 5:
    apples_price = 1.80
else:
    apples_price = 1.50    
if strawberry_kg <= 5:    
    strawberry_price = 2.50
else:
    strawberry_price = 2.20  
      
apples_price = price_item(apples_price, apples_kg)
strawberry_price = price_item(strawberry_price, strawberry_kg)

total_kg = apples_kg+strawberry_kg
total_price = apples_price+strawberry_price
deduction = 'Não atribuido'
if total_kg > 8 or total_price > 25:
    total_price = promotion_store(10, total_price)
    deduction = '10%'
    
    
print('\nMaça - {:.1f}kg\n- Preço: {:.1f}\nMorango - {:.1f}kg\n- Preço: {:.1f}\nPROMOÇÃO: {}\nTOTAL: {:.1f}'.format(apples_kg, apples_price, strawberry_kg, strawberry_price, deduction, total_price))    