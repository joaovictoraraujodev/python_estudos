import math 

#print('Neste programa vamos calcular a hipotenusa do triângulo')
#co = float(input('Digite o comprimento do Cateto Oposto do seu triângulo retângulo: '))
#ca = float(input('Digite o comprimento do Cateto Adjacente do seu triângulo retângulo: '))
#hip = (co ** 2 + ca ** 2) ** (1/2)
#print(f'O valor do cateto oposto é de {co} o do cateto adjacente {ca} resultando na hipotenusa de {hip}')

co = float(input('Digite o comprimento do Cateto Oposto do seu triângulo retângulo: '))
ca = float(input('Digite o comprimento do Cateto Adjacente do seu triângulo retângulo: '))
hip = math.hypot(co, ca)
print(f'O valor do cateto oposto é de {co} o do cateto adjacente {ca} resultando na hipotenusa de {hip}')
