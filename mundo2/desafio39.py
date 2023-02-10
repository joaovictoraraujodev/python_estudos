from datetime import date
atual = date.today().year 
nascimento = int(input('Escreva o ano em que nasceu: '))
idade = atual - nascimento
if idade == 18:
    print('Você precisa se alistar, já está na idade!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você passou da idade do alistamento, deveria ter se alistado há {saldo} anos atrás')  
else:
    saldo = idade - 18 
    print(f'Você ainda não chegou a idade do alistamento, faltam {saldo} anos')    