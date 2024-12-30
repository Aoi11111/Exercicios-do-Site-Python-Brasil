#Faça um Programa que peça os 3 lados de um 
#triângulo. O programa deverá informar se os 
#valores podem ser um triângulo. Indique, 
#caso os lados formem um triângulo, se o mesmo é:
 
#equilátero, isósceles ou escaleno.

#Dicas:

#Três lados formam um triângulo quando a soma de 
#quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

side_1 = float(input('Insira os três lados:\n'))
side_2 = float(input())
side_3 = float(input())
sum_side = side_1+ side_2

if side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
    print('Triângulo Escaleno')
elif side_1 == side_2 and side_1 == side_3 and side_2 == side_3:
    print('Triângulo Equilátero')    
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print('Triângulo Isósceles')    
elif sum_side > side_3:
    print('Triângulo')    