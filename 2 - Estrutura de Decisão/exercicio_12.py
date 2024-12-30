#Faça um programa para o cálculo de uma folha de 
#pagamento, sabendo que os descontos são do 
#Imposto de Renda, que depende do salário bruto 
#(conforme tabela abaixo) é 3% para o Sindicato 
#e que o FGTS corresponde a 11% do 
#Salário Bruto, mas não é descontado 
#(é a empresa que deposita). 

#O Salário Líquido corresponde ao Salário Bruto 
#menos os descontos. 

#O programa deverá pedir ao usuário o valor 
#da sua hora e a quantidade de horas trabalhadas 
#no mês.

#Desconto do IR:
#Salário Bruto até 900 (inclusive) 
# - isento
#Salário Bruto até 1500 (inclusive) 
# - desconto de 5%
#Salário Bruto até 2500 (inclusive) 
# - desconto de 10%
#Salário Bruto acima de 2500 
# - desconto de 20% Imprima na tela as 
#informações, dispostas conforme o exemplo abaixo. 
#No exemplo o valor da hora é 5 e a quantidade 
#de hora é 220.

#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00


print('Folha de pagamento... por favor, insira os dados abaixo.')
hourly_wage = float(input('Salário por Hora:'))
hourly_worked = float(input('Horas trabalhadas:'))

#Salário
hourly_worked = hourly_worked*5
gross_wage = hourly_worked*hourly_wage
#Desconto do IR
ir = 0
percentage_ir = 0

if gross_wage > 900 and gross_wage<=1500:
    ir = (gross_wage*5)/100
    percentage_ir = '5%'
elif gross_wage > 1500 and gross_wage<=2500:
    ir = (gross_wage*10)/100
    percentage_ir = '10%'
elif gross_wage > 2500:
    ir = (gross_wage*20)/100 
    percentage_ir = '20%'   
    
#INSS 
inss = (gross_wage*10)/100 
#FGTS
fgts = (gross_wage*11)/100
#Descontos
deduction = inss+fgts+ir
#Salário Liquido
net_wage = gross_wage-(inss+fgts+ir)



print('\nSalário Bruto: (5 * {}): R$ {}\n(-) IR ({}): R$   {}\n(-) INSS ( 10%): R$  {}\nFGTS (11%): R$  {}\nTotal de descontos: R$  {}\nSalário Liquido: R$  {}'.format(hourly_worked, gross_wage, percentage_ir, ir, inss, fgts, deduction, net_wage))
