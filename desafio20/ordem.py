import random 
print('Sorteio de ordem de apresentação de trabalho dos alunos: ')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do primeiro aluno: '))
a3 = str(input('Digite o nome do primeiro aluno: '))
a4 = str(input('Digite o nome do primeiro aluno: '))
lista = (a1, a2, a3, a4)
sorteio = random.sample((lista), k=4)
print(f'A ordem de alunos a apresentar o trabalho será: {sorteio}')
