'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima,
isto é, considere latas cheias.'''

from math import ceil

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = float((altura * largura) * 1.1)
litros = area / 6

latas = ceil(litros / 18)

galao = ceil(litros / 3.6)
total_l = latas * 80
total_g = galao * 25



print('')
print('=====comprar apenas latas de 18 litros=====')
print('Você usará {} latas de tinta para pintar {:.0f} metros quadrados.' .format(latas, area))
print('O preço total é de: R${:.2f}, custando R${} cada lata.'.format(total_l, 80.00))

print('')
print('=====comprar apenas galões de 3,6 litros=====')
print('Você usará {} galão(ões) de tinta para pintar {:.0f} metros quadrados.' .format(galao, area))
print('O preço total é de: R${:.2f}, custando R${} cada galão.'.format(total_g, 25.00))

latas_m = round(litros / 18)

print('')
print('=====Latas Mescladas=====')
if (latas_m * 18) * 6 < area:
    galao = ceil((litros % 18) / 3.6)
    total = ((latas_m * 80) + (galao * 25))
    print('Você usará {} lata(s) e {} galão(ões) para pintar {:.0f} metros quadrados.'.format(latas_m, galao, area))

    print('O valor total será de R${:.2f}, custando R${} as lata e R${} o galão.'.format(total, (latas_m * 80), (galao * 25)))
else:
    print('Você usará {} latas de tinta para pintar {:.0f} metros quadrados.'.format(latas_m, area))
    print('O preço total é de: R${:.2f}, custando R${} cada lata.'.format(total_l, 80.00))
