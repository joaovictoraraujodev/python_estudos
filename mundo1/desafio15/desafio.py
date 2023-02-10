print('Esse é um programa que calcula o quanto você ira pagar por um aluguel de automóvel')
km = float(input('Km percorridos com o carro: '))
dias = int(input('Quantidade de dias utilizando o carro: '))
rodado = km * 0.15
alugado = dias * 60
total = rodado + alugado
print(f'Sabendo que o valor por km rodado é 0,15 e a diária do carro é 60 R$, o aluguel do carro ficou no total de {total}')