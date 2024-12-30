#O Hipermercado Tabajara está com uma promoção de 
#carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#Para atender a todos os clientes, cada cliente 
#poderá levar apenas um dos tipos de carne da 
#promoção, porém não há limites para a quantidade 
#de carne por cliente. Se compra for feita no cartão
#Tabajara o cliente receberá ainda um desconto de 
#5% sobre o total da compra. Escreva um programa 
#que peça o tipo e a quantidade de carne comprada 
#pelo usuário e gere um cupom fiscal, contendo as 
#informações da compra: tipo e quantidade de carne,
#preço total, tipo de pagamento, valor do desconto 
#e valor a pagar.
from exercicio_28_27_function import promotion_store, price_item
print('Hipermercado Tabajara.\n')

while True:
   
    meat_type = input('Escolha uma das opções abaixo:\n1- File Duplo\n2- Alcatra\n3- Picanha\n') 
    meat_type.lower()

    pay_type = input('\nMetodo de pagamento:\n1- Dinheiro\n2- Cartão\n')
    pay_type.lower()

    meat_kg = float(input('Insira a quantidade em KG:\n'))
    
    if meat_type not in {'file Duplo','alcatra','picanha'} or pay_type not in {'cartão', 'dinheiro'} or meat_kg <=0:
        print('Alguma informação está inválidade. Por favor, tente novamente!')
        break

    
    if meat_type == 'file duplo':
        if meat_kg <= 5:
            meat_price = 4.90
        else:
            meat_price = 5.80   
          
    elif meat_type == 'alcatra': 
        if meat_kg <= 5:
            meat_price = 5.90
        else:
            meat_price = 6.80  
         
    elif meat_type == 'picanha':
        if meat_kg <= 5:
            meat_price = 6.90
        else:
            meat_price = 7.80 

    meat_price = price_item(meat_price, meat_kg) 
    meat_deduction = meat_price 
    deduction = 'Não atribuido.'
      
    if pay_type == 'cartão':
        meat_deduction = promotion_store(5, meat_price)
        deduction = '5%'

    meat_type = meat_type.capitalize()
    pay_type = pay_type.capitalize()
    
    print("""
         \nCupom Fiscal -------------
          {} - {}kg
          Forma de Pagamento: {}
          Preço: R${:.1f}
          Desconto: {}
          ------------- Preço Total: R${:.1f}
          """.format(meat_type, meat_kg, pay_type, meat_price, deduction, meat_deduction))
    break   
