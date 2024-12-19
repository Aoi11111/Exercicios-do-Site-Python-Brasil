#Tendo como dados de entrada a altura de uma 
#pessoa, construa um algoritmo que calcule seu 
#peso ideal, usando a seguinte fórmula: 
#(72.7*altura) - 58

height = float(input('Insira sua altura:'))

calc = (72.7*height) - 58
print('Seu peso ideal é: {:.2f}'.format(calc))