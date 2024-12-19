#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

import numpy

s1 = float(input('Insira as suas 4 notas bimestrais:'))
s2 = float(input())
s3 = float(input())
s4 = float(input())

scores = [s1, s2, s3, s4]

def median_scores(s_list):
    result = numpy.mean(s_list)
    return result

print('A média é: ', median_scores(scores))