#Altere o programa anterior para mostrar no 
#final a soma dos números. 

start = int(input('Insira dois números inteiros:\n'))
end = int(input())

print('\n')

sum_num = 0

for i in range(start+1, end):
    sum_num += i
    print(i)
    
print('Soma:', sum_num)    