#Faça um programa que leia um nome de usuário e a 
#sua senha e não aceite a senha igual ao nome do 
#usuário, mostrando uma mensagem de erro e voltando 
#a pedir as informações.



while True:
    user_name = input('\nInsira seu nome e senha:\n')
    password = input()
    
    if user_name == password:
        print('O nome e a senha não podem ser o mesmo, tente novamente.')
    else:
        print('Cadastro completo.')
        break    