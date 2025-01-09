def fibonacci(max):
    list_fibonacci = [1]
    a, b = 0, 1
    if max == 0:
        list_fibonacci = ['Vazio']
        return list_fibonacci
    elif max == 1:
        return list_fibonacci
    elif max == 2:
        list_fibonacci = [1, 1]
        return list_fibonacci
    else:
        for i in range(max):
            a, b = b, b+a
            list_fibonacci.append(b)
        
        return list_fibonacci  