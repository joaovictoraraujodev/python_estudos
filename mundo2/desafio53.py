print('-='* 50)
print('Esse é um programa que define se a palavra digitada é ou não um palíndromo')
print('-='* 50)
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto [letra]
if inverso == junto:
    print(f'O inverso de {junto} é {inverso}!')
else: 
    print('Não é um palíndromo!')        