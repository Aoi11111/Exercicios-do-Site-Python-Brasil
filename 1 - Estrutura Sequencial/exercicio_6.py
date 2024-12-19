#Faça um Programa que peça o raio de um círculo, 
#calcule e mostre sua área.
 

from math import pi

circle_radius = float(input('Insira o raio do circulo:'))

def circle_area(c):
    
    result = round(pi * (c**2))
    return result

print('A area do circulo é:', circle_area(circle_radius))

