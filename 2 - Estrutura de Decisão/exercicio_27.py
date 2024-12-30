#Um posto está vendendo combustíveis com a seguinte
#tabela de descontos:

#Álcool:

#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro

#Gasolina:

#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro 

#Escreva um algoritmo que leia o número de litros 
#vendidos, o tipo de combustível 
#(codificado da seguinte forma: A-álcool, 
#G-gasolina), 

#calcule e imprima o valor a ser pago pelo cliente 
#sabendo-se que o preço do litro da gasolina é 
#R$ 2,50 o preço do litro do álcool é R$ 1,90.
def promotion_store(promotion, price):
    deduction = price * (promotion/100) 
    price = price - deduction
    return price
 
print('Bem vindo ao posto!')

gasoline_type = input("""
               Do que você precisa?
               A - Alcool
               G - Gasolina
               \n""")
liters = int(input('Quantos litros?\n'))
price = 0

if gasoline_type == 'A' or gasoline_type == 'a':
    for i in range(liters):
            price += 2.50
            
    if liters <= 20:
        price = promotion_store(4, price)
    else:
        price = promotion_store(6, price)
        
elif gasoline_type == 'G' or gasoline_type == 'g':
    for i in range(liters):
            price += 1.90
            
    if liters <= 20:
        price = promotion_store(3, price)
    else:
        price = promotion_store(5, price)   
else:
    print('Valor Inválido, tente novamente.')    
    
print('Valor Total: {:.1f}'.format(price))    