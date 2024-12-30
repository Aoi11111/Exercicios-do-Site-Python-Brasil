#Faça um Programa para um caixa eletrônico. 

#O programa deverá perguntar ao usuário o valor
#do saque e depois informar quantas notas de 
#cada valor serão fornecidas. As notas 
#disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o
#máximo de 600 reais. O programa não deve se 
#preocupar com a quantidade de notas existentes
#na máquina.

print('Bem vindo a Caixa Eletrônica!')
print('O valor mínimo é 10 e o máximo 600.')
money = int(input('Insira o valor requerido:\n'))

if money < 10 or money > 600:
    print('\nSinto muito, valor inválido.')
else:
    cents_1 = 0
    cents_5 = 0
    paper_money_10 = 0
    paper_money_50 = 0
    paper_money_100 = 0   
    
    while money > 100:
        money -=100
        paper_money_100 += 1
    while money > 50:
        money -=50
        paper_money_50 += 1
    while money > 10:
        money -=10
        paper_money_10 += 1
    while money > 5:
        money -=5
        cents_5 += 1
    while money > 1:
        money -=1
        cents_1 += 1     
    
            
    print('Notas de 10 reais:',paper_money_10)
    print('Notas de 50 reais:',paper_money_50)
    print('Notas de 100 reais:',paper_money_100)
    print('centavos em 1:',cents_1)
    print('centavos em 5:',cents_5)
       