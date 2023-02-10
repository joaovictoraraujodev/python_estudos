print('Este é um programa que calcula quantos liros de tinta você ira gastar para pintar sua parede!')
n1 = float(input('Digite a largura da sua parede: '))
n2 = float(input('Digite a altura da sua parede: '))
a = n1 * n2
t = a / 2
print(f'Somando a largura {n1} e a altura {n2} temos a área no valor de {a} onde para pintar essa área será necessário {t} litros de tinta já que 1 litro de tinta pinta 2m²')