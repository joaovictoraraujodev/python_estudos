#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('Radar eletrônico')
velocidade = float(input('Digite a velocidade do carro: ')) 
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
else:
    print('Tenha um bom dia! Dirija com segurança!')    
multa = (velocidade - 80) * 7
print(f'Você recebeu uma multa no valor de {multa}')