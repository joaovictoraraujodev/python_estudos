print('Esse programa identifca se sua cidade tem a palavra Santo: ')
nome = input('Digite o nome da sua cidade: ')
verificar = "Santo" in nome
if verificar==True:
    print('Sua cidade começa com a palavra Santo!')
else:
    print('Sua cidade não começa com a palavra Santo!')