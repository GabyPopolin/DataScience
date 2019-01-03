'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))
media = (n1 + n2 + n3 + n4)/4

print('')
print('A média final do aluno é: {:.2f}' .format(media))