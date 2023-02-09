salario = float(input('Digite o valor do seu salário para calcular o aumento: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava: {salario} passara a ganhar: {novo}')    


