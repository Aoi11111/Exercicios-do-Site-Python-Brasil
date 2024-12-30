#Faça um programa que pergunte o preço de 
#três produtos e informe qual produto 
#você deve comprar, sabendo que a decisão é 
#sempre pelo mais barato.

price_1 = float(input('Insira o preço de três produtos:'))
price_2 = float(input())
price_3 = float(input())

#Metodo com listas
#prices_products = [price_1, price_2, price_3]

#min_price = min(prices_products)
#print('A compra mais barata é R${} reais'.format(min_price))

#Metodo pedido pelo exercicio

if price_1 < price_2 and price_1 < price_3:
    print('A compra mais barata é R${} reais'.format(price_1))
elif price_2 < price_3:
    print('A compra mais barata é R${} reais'.format(price_2)) 
else:
    print('A compra mais barata é R${} reais'.format(price_3)) 