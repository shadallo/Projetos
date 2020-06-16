"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres:(62.1*h) - 44.7
"""

sexo = input('Digite "1" para Mulher, e "2" para Homen:')

if sexo == '2':
    altura = float(input('Digite sua altura em metros, separado por ponto (ex: 1.60):'))
    print('Peso Ideal é:', ((72.7 * altura) - 58))
elif sexo == '1':
    altura = float(input('Digite sua altura em metros, separado por ponto (ex: 1.60):'))
    print('Peso ideal é:', ((62.1 * altura) - 44.7))
