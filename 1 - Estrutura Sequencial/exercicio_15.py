#Faça um Programa que pergunte quanto você ganha 
#por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o 
#Imposto de Renda, 8% para o INSS e 5% para o 
#sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.

#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

#Obs.: Salário Bruto - Descontos = Salário Líquido.

wage = float(input('Insira quanto você ganha por hora e as horas trabalhadas:'))
hours = float(input()) 
  
#Salário Bruto
hours_worked = hours * 5
gain = wage*hours_worked  

#IR
ir = (gain*11)/100

#INSS
inss = (gain*8)/100

#Sindicato
sind = (gain*5)/100

#Salário Liquido
salario_liquido = ((gain-ir)-inss)-sind
      
print('+ Salário Bruto : R${:.1f}\n - IR (11%) : R${:.1f} \n - INSS (8%) : R${:.1f} \n - Sindicato (5%) : R${:.1f} \n = Salário Liquido : R${}'.format(gain, ir, inss, sind,salario_liquido))