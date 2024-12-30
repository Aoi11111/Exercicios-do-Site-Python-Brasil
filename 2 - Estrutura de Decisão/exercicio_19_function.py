

def units(num):
    
    num = str(num)
    
    
    if len(num) == 3:
        
        unit = num[2:3]
        ten = num[1:2]
        hundred = num[0:1]
        
        return unit, ten, hundred
    elif len(num) == 2:
        
        unit = num[1:2]
        ten = num[0:1]
        
        return unit, ten
    elif len(num) == 1:
        
        unit = num[0:1]
        return unit  
        
    

