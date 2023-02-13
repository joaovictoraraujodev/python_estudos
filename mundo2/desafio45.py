from random import randint  
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-=' * 30)
print(''' Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=' * 30)
jogador = int(input('Qual é a sua jogada ?'))
print('-=' * 30)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA')    

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA')        

elif computador == 2:
    if jogador == 0:    
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')                