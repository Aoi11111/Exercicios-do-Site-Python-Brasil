#Observando os termos no plural a colocação do "e", da vírgula entre outros. 
#Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar 
#com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


from exercicio_19_function import units

list_nums = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for i in list_nums:
    
    len_i = len(str(i))
    
    if len_i == 3:
        unit, ten, hundred  = units(i)
        
        hundred = int(hundred)
        ten = int(ten)
        unit = int(unit)
    elif len_i == 2:     
       unit, ten = units(i) 
       
       ten = int(ten)
       unit = int(unit)
    elif len_i == 1:
        unit  = units(i)
        
        unit = int(unit)
    
    
    hundred = int(hundred)
    ten = int(ten)
    unit = int(unit)
    
    if hundred > 1 or hundred == 0:
        h_word = 'centenas'
    else:
        h_word = 'centena'    
        
    if ten > 1 or ten == 0:
        t_word = 'dezenas'
    else:
        t_word = 'dezena' 
        
    if unit > 1 or unit == 0:       
       u_word = 'unidades'
    else:
       u_word = 'unidade'   
    
    
    
    if len_i == 3:
        print('\n- {} {}, {} {} e {} {}'.format(hundred, h_word, ten, t_word, unit, u_word))
    elif len_i == 2:     
       print('\n- {} {} e {} {}'.format(ten, t_word, unit, u_word))  
    elif len_i == 1:
        print('\n- {} {}'.format(unit, u_word))
