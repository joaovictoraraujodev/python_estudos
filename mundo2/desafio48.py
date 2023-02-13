print('-=' * 30)
print('Esse é um programa que calcula a soma entre todos os número impares que são múltiplos de 3')
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}')