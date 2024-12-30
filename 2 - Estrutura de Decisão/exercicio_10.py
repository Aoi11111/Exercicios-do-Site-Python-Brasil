#Faça um Programa que pergunte em que turno 
#você estuda. 

#Peça para digitar:
#M-matutino 
#ou V-Vespertino 
#ou N- Noturno. 

#Imprima a mensagem 
#"Bom Dia!" 
#"Boa Tarde!" 
#ou "Boa Noite!" 
#ou "Valor Inválido!", conforme o caso.

 
print('Em que horário você estuda?')
print('* M - matutino \n* V - Vespertino \n* N - Noturno')
shift = input()
shift = shift.upper()     
    
if shift == 'M':
    print('Bom dia!')
elif shift == 'V':
    print('Boa Tarde!') 
elif shift == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')    

          

