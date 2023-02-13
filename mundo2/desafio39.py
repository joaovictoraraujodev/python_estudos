from datetime import date
atual = date.today().year 
nascimento = int(input('Escreva o ano em que nasceu: '))
idade = atual - nascimento
if idade == 18:
    print(f'Você tem {idade} precisa se alistar, já está na idade!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você tem {idade} e deveria ter se alistado há {saldo} anos atrás')  
else:
    saldo = idade - 18 
    print(f'Você tem {idade} ainda não chegou na idade do alistamento, faltam {saldo} anos')    