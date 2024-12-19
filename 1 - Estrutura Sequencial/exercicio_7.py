#Faça um Programa que calcule a área de um quadrado, 
#em seguida mostre o dobro desta área para o 
#usuário.

side_square = float(input('Digite a medida de um dos lados do quadrado:'))

def area_square_double(s):
    result = s**2
    double_area = round(result*2)
    return double_area

print('O dobro da área do quadrado é:', area_square_double(side_square))    
