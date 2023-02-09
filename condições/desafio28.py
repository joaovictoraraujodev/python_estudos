from random import randint
computador = randint(0, 5)
print('Esse é um jogo de adivinhação, escolha um número de 0 a 5 e tente adivinhar')
jogador = int(input('Digite um número: '))
print('Processando o número...')
if computador == jogador:
    print('Parabéns você adivinhou o número!')
else:
    print('Você errou, tente novamente!')    