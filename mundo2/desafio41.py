from datetime import date
atual = date.today().year
nascimento = float(input('Digite o ano de seu nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade <=14:
    print('Você está na categoria INFATIL')
elif idade <=19:
    print('Você está na categoria JUNIOR')    
elif idade <= 25:
    print('Você está na categoria SÊNIOR') 
else:
    print('Você está na categoria MASTER')     