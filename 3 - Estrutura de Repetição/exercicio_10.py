#Faça um programa que receba dois números 
#inteiros e gere os números inteiros que 
#estão no intervalo compreendido por eles.


start = int(input('Insira dois números inteiros:\n'))
end = int(input())

print('\n')


for i in range(start+1, end):
    print(i)