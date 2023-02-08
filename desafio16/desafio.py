#crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
import math
n = float(input('Digite um número real que será convertido para sua parte inteira: '))
print(f'O valor do número real é {n} e convertendo para parte sua parte inteira é {math.floor(n)}')