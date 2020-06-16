"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1 - o produto do dobro do primeiro com metade do segundo .
2 - a soma do triplo do primeiro com o terceiro.
3 - o terceiro elevado ao cubo.
"""
primeiro_num = int(input('Digite 1º Número Inteiro:'))
segundo_num = int(input('Digite 2º Número Inteiro:'))
terceiro_num = float(input('Digite um Número Real:'))

print('Produto:', ((primeiro_num*2)*(segundo_num/2)))
print('Soma:', (primeiro_num*3)+terceiro_num)
print('Cubo:', (terceiro_num**3))

