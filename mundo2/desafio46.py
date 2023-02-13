from time import sleep
print('''FOGOS DE ARTIFICIO:
[1] INICIAR CONTAGEM REGRESSIVA.
[2] NÃO EXPLODIR OS FOGOS''')
opção = int(input('Digite sua opção: '))
sleep(1)
if opção == 1:
    for c in range (10, 0, -1):
        sleep(1)
        print(c)    
    print('FELIZ ANO NOVO!')   
else:
    print('Você não quis soltar os fogos.')    
