#Faça um programa que lê as duas notas parciais 
#obtidas por um aluno numa disciplina 
#ao longo de um semestre, e calcule a sua média. 
#A atribuição de conceitos obedece à tabela abaixo:

#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

#O algoritmo deve mostrar na tela as notas, a 
#média, o conceito correspondente e 
#a mensagem “APROVADO” se o conceito for A, B ou 
#C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('Insira suas notas:\n'))
n2 = float(input())

mean_notes = (n1+n2)/2

note = ''
approval = ''

if mean_notes > 0 and mean_notes < 4:
    note = 'E'
    approval = 'REPROVADO'
elif mean_notes > 4 and mean_notes < 6:
    note = 'D'
    approval = 'REPROVADO'  
elif mean_notes > 6 and mean_notes < 7.5:
    note = 'C'
    approval = 'APROVADO'
elif mean_notes > 7.5 and mean_notes < 9:
    note = 'B'
    approval = 'APROVADO'
elif mean_notes > 9 and mean_notes < 10:
    note = 'A'
    approval = 'APROVADO'               
    
print('\n- Nota 1: {}\n- Nota 2: {}\n- Média: {}\n- Conceito: {}\nVocê está {}!'.format(n1, n2,mean_notes, note, approval))


