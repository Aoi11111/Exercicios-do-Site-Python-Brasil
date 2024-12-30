#Faça um Programa que verifique se uma letra 
#digitada é vogal ou consoante.

letter = input('Insira uma letra:')
letter.lower()

def check_vowel(v):
    if len(v) > 1:
        return print('Você escreveu mais de uma letra, tente novamente.')
    elif v in "aeiou":
        return print('É uma vogal')
    else:
        return print('É uma consoante.')    
        
print(check_vowel(letter))        
