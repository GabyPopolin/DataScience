'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).'''

f = float(input('Digite a temperatura em graus Farenheit: '))
#c = (f - 32) * 5/9
c = (5 * (f-32) / 9)

print('')
print('A transformação da temperatura de Farenheit para Celsius é de {:.1f}' .format(c))
