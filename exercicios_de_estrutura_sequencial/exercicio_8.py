"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
valor_hora = float(input('Quanto você ganha por Hora:'))
horas_trabalhada = float(input('Quantas Horas trabalhou no Mês:'))

salario = valor_hora * horas_trabalhada

print("Seu Salário é:R$", salario)
