#Tendo como dado de entrada a altura (h) de uma 
#pessoa, construa um algoritmo que calcule seu 
#peso ideal, utilizando as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

height = float(input('Insira sua altura e seu gênero:'))
gender = input()
gender.lower()

calc_m = (72.7*height) - 58
calc_w = (62.1*height) - 44.7

if gender == 'mulher' or 'feminino':
    print('Seu peso ideal é: {:.1f}'.format(calc_w))
elif gender == 'homem' or 'masculino':
    print('Seu peso ideal é: {:.1f}'.format(calc_m)) 
else:
    print('Erro, tente de novo') 