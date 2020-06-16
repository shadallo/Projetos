"""
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

temperatura = float(input('Digite a Temperatura:'))
temp_celsius = ((temperatura - 32) * 5 / 9)

print('A Temperatura em Celsius é:', temp_celsius, 'ºC')
