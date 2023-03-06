print('-=-'*30)
print('Este programa lê um número inteiro e diz se é um número primo!')
print('-=-'*30)
num = int(input('Digite um número inteiro: '))
mult = 0
for c in range(2,num):
    if (num % c == 0):
        print('Multiplo de', c)
        mult += 1
if (mult==0):
    print('É primo')
else:
    print('Tem', mult,'múltiplos acima de 2 e abaixo de', num)    