#Faça um programa que peça o tamanho de um 
#arquivo para download (em MB) e a velocidade 
#de um link de Internet (em Mbps), calcule e 
#informe o tempo aproximado de download do 
#arquivo usando este link (em minutos).

size_mb = float(input('Insira o tamanho do arquivo em MB:'))
speed = float(input('Insira a velocidade da internet em MBps:'))

time_dowload = (size_mb/speed)*60
print('O tempo de dowload será de {:.1f} minutos'.format(time_dowload))