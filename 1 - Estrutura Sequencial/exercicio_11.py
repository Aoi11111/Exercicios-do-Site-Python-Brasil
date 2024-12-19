#Faça um Programa que peça 2 números inteiros e um número real. 

# Calcule e mostre:
#A / o produto do dobro do primeiro com metade do segundo .
#B / a soma do triplo do primeiro com o terceiro.
#C / o terceiro elevado ao cubo.

n1 = int(input('Insira dois numeros inteiros e um real:'))
n2 = int(input())
n3 = float(input())

a = n1**2 + (n2/2)
print('\nO produto do dobro do {} com metade do {}: {:.1f}'.format(n1, n2, a))

b = n1**3 + n3
print('a soma do triplo do {} com o {}: {:.1f}'.format(n1, n3, b))

c = n3**3
print("{} elevado ao cubo: {:.1f}".format(n3, c))
