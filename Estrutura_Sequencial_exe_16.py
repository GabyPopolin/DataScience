'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
from math import ceil

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

litros = (altura * largura) / 3

valor_litro = 80.0
quant_litro = 18

latas = ceil(litros / quant_litro)

print('')
print('Você usará {} latas de tinta' .format(latas))
print('O preço total é de: R${:.2f}'.format(latas * valor_litro))