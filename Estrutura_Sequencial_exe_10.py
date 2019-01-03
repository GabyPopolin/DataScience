'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.'''

c = float(input('Digite a temperatura em graus Celsius: '))
f = (c * 9/5) + 32

print('')
print('Graus Celsius:',c)
print('A transformação da temperatura de Celsius para Farenheité de {:.1f}' .format(f))
