'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7'''

genero = str(input('Você é homem ou mulher? '))
altura = float(input('Digite aqui sua altura em metros: '))
altura_h = (72.7*altura) - 58
altura_m = (62.1*altura) - 44.7

if genero == 'mulher':
    print('Seu peso ideal é de {:.2f}kg' .format(altura_m))
elif genero == 'homem':
    print('Seu peso ideal é de {:.2f}kg.' .format(altura_h))
else:
    print('Favor, informar gênero com valores válidos!!!!!')