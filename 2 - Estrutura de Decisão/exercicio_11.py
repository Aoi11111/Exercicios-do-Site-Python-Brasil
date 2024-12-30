#As Organizações Tabajara resolveram dar um 
#aumento de salário aos seus colaboradores e 
#lhe contraram para desenvolver o programa que 
#calculará os reajustes.

#Faça um programa que recebe o salário de um 
#colaborador e o reajuste segundo o seguinte 
#critério, baseado no salário atual:

#salários até R$ 280,00 (incluindo) : 
#aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : 
#aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : 
#aumento de 10%
#salários de R$ 1500,00 em diante : 
#aumento de 5% 

#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

wage = float(input('Insira o seu salário:'))

if wage <= 280:
    readjustment = wage*1.20
    percentage = '20%'
elif wage > 280 and wage < 700:
    readjustment = wage*1.15  
    percentage = '15%' 
elif wage > 700 and wage < 1500:
    readjustment = wage*1.10
    percentage = '10%'
elif wage >= 1500:
    readjustment = wage*1.5 
    percentage = '5%'   
    
increase = readjustment-wage  
print('\n- Salário Anterior: {}\n- Percentual: {}\n- Aumento: {:.1f}\n- Salário Atual: {:.1f}'.format(wage, percentage, increase, readjustment ))       
    