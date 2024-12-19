#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

earning_per_hour = float(input('Insira quanto você ganha por hora e as horas trabalhadas:'))
hours = float(input()) 

def calc_wage(w, h):
      hours_worked = h * 5
      gain = w*hours_worked
      return gain
      
print('O total do salário é:', calc_wage(earning_per_hour, hours)) 