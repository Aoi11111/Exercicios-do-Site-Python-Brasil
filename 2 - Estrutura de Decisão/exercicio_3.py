#Faça um Programa que verifique se uma letra 
#digitada é "F" ou "M". 

#Conforme a letra escrever: 
# F - Feminino, 
# M - Masculino, 
# Sexo Inválido.

gender = input('Insira f para feminino ou m para masculino.')
gender = gender.lower()

if gender == 'f':
    print('Feminino')
elif gender == 'm':
    print('Masculino')
else:
    print('Inválido, tente novamente.')        
