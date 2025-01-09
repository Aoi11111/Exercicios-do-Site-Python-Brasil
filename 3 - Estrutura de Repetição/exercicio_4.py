#Supondo que a população de um país A seja 
#da ordem de 80000 habitantes com uma taxa 
#anual de crescimento de 3% e que a população
#de B seja 200000 habitantes com uma taxa de 
#crescimento de 1.5%. Faça um programa que 
#calcule e escreva o número de anos necessários
#para que a população do país A ultrapasse ou 
#iguale a população do país B, mantidas as taxas
#de crescimento.

population_A = 80000
population_B = 200000
years = 0

while population_B > population_A:
    growth_A = population_A*0.03
    growth_B = population_B*0.015
    
    population_A+=growth_A
    population_B+=growth_B
    years+=1
    print('\nAno: {}\nPopulação A: {:.1f}\nPopulação B: {:.1f}'.format(years, population_A, population_B))
    
print('\nPopulação A ultrapassa População B em {} anos'.format(years))    