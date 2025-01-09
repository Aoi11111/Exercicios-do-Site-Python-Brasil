#Faça um programa que leia e valide as seguintes 
#informações:

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

print('\nPreencha as informações a seguir:')

user_name = input('\nNome:\n') 
while (len(user_name) < 3):
    user_name = input('Valor inválido, insira um nome maior que 3 caracteres:\n')      

age = int(input('Idade:\n'))  
while (age < 0 or age > 150):
    age = int(input('Idade inválida, insira sua idade real:\n')) 
         
wage = float(input('Salário:\n'))
while (wage <=0):
    wage = float(input('Insira um salário válido:\n'))    
    
gender = input('Sexo (f ou m):\n')
while (gender not in {'m', 'f'}):
    gender = input('Por favor, insira um valor válido entre f ou m:\n')

marital_status = input('Estado Civil (s, c, v ou d):\n')
while ( marital_status not in {'s', 'c', 'v', 'd'}):
    marital_status = input('Por favor, insira um valor válido entre s, c, v ou d:\n')
    
print('Cadastro Completo.')
        
                  
    

