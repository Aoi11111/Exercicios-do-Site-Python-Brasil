#Faça um Programa que converta metros para centímetros.
meter = float(input('Insira um numero em metros:'))


def meter_to_centimeter(m):
    result = m * 100
    return result

print('Em centimetros é:', meter_to_centimeter(meter))