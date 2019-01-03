'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input('Digite aqui quanto você ganha por hora no seu trabalho: '))
horas_trabalhadas = float(input('Digite aqui quantas horas você trabalha por mês: '))
total = valor_hora * horas_trabalhadas

print('')
print('O seu salário referente ao mês trabalhado será de R${:.2f}' .format(total))