#Faça um Programa que peça uma data no formato 
#dd/mm/aaaa e determine se a mesma é uma data 
#válida.
import datetime

while True:
    print('\nInforme a data, formato(dd/mm/aaaa):')
    date = list(input())

    #Verificando o formato
    if len(date) != 10:
        print('\n- Formato incorreto.')
        break
    
    #Separando as informações
    day = ''
    month = ''
    year = ''

    for i in range(len(date)):
        if i < 2:
            day += date[i]
        elif i > 2 and i < 5:
            month += date[i]    
        elif i > 5:
            year += date[i]   
        
    day = int(day)
    month = int(month)
    year = int(year)
    
    #Ano atual
    date_now = datetime.datetime.now()
    year_now = date_now.year

    #Verificação mês, ano e dia
    if month > 12:
        print('- Mês Incorreto.')
    elif year > year_now:
        print('- Ano Incorreto, {} ainda não aconteceu.'.format(year))  
    elif day > 31:
        print('- Dia Incorreto.') 
    elif month == 11 and day > 30 or month == 9 and day > 30 or month == 6 and day > 30 or month == 4 and day > 30:
        print('- Data Incorreta, nos meses 4, 6, 9 e 11 há até 30 dias.')
    elif month == 2 and day > 28 or month == 2 and year%4 == 0 or year%400 == 0 and day > 29:
        print('- Data Incorreta, fevereiro tem 28 dias, em anos bissextos em 29 dias.')    
    else:
        print('Esta data é válida.')   
        break 
    
