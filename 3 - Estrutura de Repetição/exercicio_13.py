#Faça um programa que peça dois números, base e 
#expoente, calcule e mostre o primeiro número 
#elevado ao segundo número. Não utilize a função 
#de potência da linguagem.

base = int(input('Informe a base:\n'))
exponent = int(input('Informe o expoente:\n'))

result = 1

for i in range(exponent):
    result = base * base
    result = base * result 

print('Resultado: ', result)