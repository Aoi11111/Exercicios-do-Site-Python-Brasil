#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação 
#sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 
#questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
#5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

guilt_meter = 0
answer = []

print('Investigação Criminal, por favor, responda com sinceridade.\n')

ask = input('Telefonou para a vítima?\n')
answer.append(ask)
ask = input('Esteve no local do crime?\n')
answer.append(ask)
ask = input('Mora perto da vítima?\n')
answer.append(ask)
ask = input('Devia para a vítima?\n')
answer.append(ask)
ask = input('Já trabalhou com a vítima?\n')
answer.append(ask)

for i in answer:
    if i == 's' or i == 'S' or i == 'sim' or i == 'SIM' or i == 'Sim':
        guilt_meter += 1
        
if guilt_meter == 5:
    print('Você é o assasino!')   
elif guilt_meter >= 3 and guilt_meter <= 4:
    print('Você é cúmplice!')          
elif guilt_meter == 2:
    print('Você é suspeito!')    
else:
    print('Você é inocente!')    