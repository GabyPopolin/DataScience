'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Digite aqui quanto você ganha por hora no seu trabalho: '))
horas_trabalhadas = float(input('Digite aqui quantas horas você trabalha por mês: '))
bruto = valor_hora * horas_trabalhadas
ir = (bruto * 11) / 100
inss = (bruto * 8) / 100
sind = (bruto * 5) / 100
liquido = bruto - ir - inss - sind

print('')
print('Salário Bruto: R${:.2f}' .format(bruto))
print('Imposto de Renda (11%): R${:.2f}' .format(ir))
print('INSS (8%): R${:.2f}' .format(inss))
print('Sindicato (5%): R${:.2f}' .format(sind))
print('Salário Líquido: R${:.2f}' .format(liquido))