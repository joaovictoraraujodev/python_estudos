#Estrutura condicional aninhada
nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que nome lindo que você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem feio!')
elif nome in 'Ana Cláudia Jéssica Julia':
    print('Belo nome feminino!')    
else:
    print('Seu nome é comum!') 