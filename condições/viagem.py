km = float(input('Qual a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {km}')
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.25
print(f'O valor da sua passagem será {preço}')