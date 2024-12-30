#Faça um programa para a leitura de duas 
#notas parciais de um aluno. 
#O programa deve calcular a média alcançada 
#por aluno e apresentar:

#A mensagem "Aprovado", se a média alcançada 
#for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor 
#do que sete;
#A mensagem "Aprovado com Distinção", se a 
#média for igual a dez.

score_1 = float(input('Insira suas notas:'))
score_2 = float(input())

media = (score_1+score_2)/2
print('\nSua média é {}, logo você está:'.format(media))

if media < 7:
    print('- Reprovado.')
elif media == 10:
    print('- Aprovado com Distinção.')  
else:
    print('- Aprovado.')      