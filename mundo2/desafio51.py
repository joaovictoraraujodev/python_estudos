print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao
for c in range (num, decimo, razao):
    print(f'{c}', end=' -> ')
print('ACABOU')    