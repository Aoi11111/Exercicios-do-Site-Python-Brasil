#Altere o programa anterior permitindo ao 
#usuário informar as populações e as taxas 
#de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

while True:
    print('\nInsira as informações abaixo:')
    
    population_A = float(input('População de A:\n'))
    growth_rate_A = float(input('Taxa de Crescimento da população:\n'))
    
    population_B = float(input('População de B:\n'))
    growth_rate_B = float(input('Taxa de Crescimento da população:\n'))
    
    years = 0
    growth_A = 0
    growth_B = 0

    while population_B > population_A:
        growth_A = population_A*(growth_rate_A/100)
        growth_B = population_B*(growth_rate_B/100)
    
        population_A+=growth_A
        population_B+=growth_B
        years+=1
        print('\nAno: {}\nPopulação A: {:.1f}\nPopulação B: {:.1f}'.format(years, population_A, population_B))
    
    print('\nPopulação A ultrapassa População B em {} anos'.format(years))    
    
    end = input('Deseja recomeçar? (s ou n)\n')
    if end in {'n', 'não', 'nao'}:
        break

print('Fim de jogo....')  