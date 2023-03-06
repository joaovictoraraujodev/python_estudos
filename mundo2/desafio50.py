soma = 0 
conta = 0
for c in range (1,7):
    num = int(input('Digit um valor: '))
    if num % 2 ==0:
        soma += num
        conta += 1
print(f'Você informou {conta} números pares e a soma foi de {soma}')        


