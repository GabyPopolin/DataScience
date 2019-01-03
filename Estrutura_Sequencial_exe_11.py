'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

n1 = int(input('Digite um número inteiro aqui: '))
n2 = int(input('Digite aqui também um outro número inteiro: '))
n3 = float(input('Digite um número real aqui: '))
a = (n1 * 2) + (n2 / 2)
b = (n1 * 3) + (n3)
c = n3 ** 3

print('')
print('=====Produto do dobro do primeiro com metade do segundo=====')
print('({} * 2) + ({} / 2)' .format(n1, n2))
print(a ,'ou {} e {}'.format(n1*2, n2/2) )

print('')
print('=====Soma do triplo do primeiro com o terceiro=====')
print('({} * 3) + {}' .format(n1, n2))
print(b)

print('')
print('=====Terceiro elevado ao cubo=====')
print('{} ** 3' .format(n3))
print('{:.2f}' .format(c))