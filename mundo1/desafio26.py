palavra = input('Digite uma palavra: ')
a = palavra.count('a')
local1 = palavra.find('a')
local2 = palavra.rfind('a')
print(f'Sua palavra contém {a} letra(s) "a"')
print(f'A primeira letra "a" está na posição {local1 + 1}')
print(f'A última letra "a" está na posição {local2 + 1}')
