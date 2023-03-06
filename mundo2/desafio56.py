# Inicializando variáveis
soma_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_de_20 = 0

# Loop para ler os dados de 4 pessoas
for i in range(4):
    print(f'Insira os dados da {i+1}ª pessoa:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ')

    # Soma as idades para calcular a média depois
    soma_idade += idade

    # Verifica se a pessoa é homem e se é mais velho que o atual mais velho
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Verifica se a pessoa é mulher e tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

# Calcula a média das idades
media_idade = soma_idade / 4

# Imprime os resultados
print(f'\nMédia de idade: {media_idade:.2f}')
if nome_homem_mais_velho:
    print(f'Homem mais velho: {nome_homem_mais_velho}')
else:
    print('Não foram inseridos homens')
print(f'Mulheres com menos de 20 anos: {mulheres_menos_de_20}')