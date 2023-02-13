num = int(input('Digite um número para descobrir se é ímpar ou par: '))
print(f'O número digitado é {num}')
resultado = num % 2
if resultado == 0:
    print('O resultado é par!')
else:
    print('O resultado é ímpar!')
