'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

from math import ceil

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = (altura * largura)
litros = area / 6

valor_lata = 80.0
quant_lata = 18

valor_galao = 25.00
quant_galao = 3.6

latas = ceil(litros / quant_lata)
galao = ceil(litros / quant_galao)

terceira = (area % 6)

print('')
print(area)
print('{:.0f}' .format(litros))
print('{:.0f}' .format(terceira))
print('')

print('')
print('=====comprar apenas latas de 18 litros=====')
print('Você usará {} latas de tinta' .format(latas))
print('O preço total é de: R${:.2f}'.format(latas * valor_lata))

print('')
print('=====comprar apenas galões de 3,6 litros=====')
print('Você usará {} galão(ões) de tinta' .format(galao))
print('O preço total é de: R${:.2f}'.format(galao * valor_galao))


print('')
print('=====Menor Preço=====')
if (area % 18) == 0:
    print('Você usará {} latas de tinta' .format(latas))
    print('O preço total é de: R${:.2f}'.format(latas * valor_lata))
else:
    print('Você usará {} latas de tinta e {} galão(ões) de tinta.'.format(galao, latas))
    print('O preço total é de: R${:.2f}'.format((latas * valor_lata) + (galao * valor_galao)))