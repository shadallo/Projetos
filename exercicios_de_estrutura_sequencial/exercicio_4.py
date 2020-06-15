"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def media_bimestral(nota_1, nota_2, nota_3, nota_4):
    return (nota_1 + nota_2 + nota_3 + nota_4) / 4


nota_1 = float(input('Digite a nota do 1º Bimestre:'))
nota_2 = float(input('Digite a nota do 2º Bimestre:'))
nota_3 = float(input('Digite a nota do 3º Bimestre:'))
nota_4 = float(input('Digite a nota do 4º Bimestre:'))

print('A Média do Bimestre foi:', media_bimestral(nota_1, nota_2, nota_3, nota_4))
