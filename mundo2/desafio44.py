print('-=' * 30)
print('Lojas JOÃO')
print('-=' * 30)
preço = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque 10% de desconto
[2] à visto no cartão 5% de desconto
[3] em até 2x no cartão é o preço normal
[4] 3x ou mais no cartão: 20% de juros''')
print('-=' * 30)
opção = int(input('Digite a opção de pagamento: '))
if opção == 1:
    total = preço - (preço * 10) / 100
    print(f'sua compra no valor de {preço} terá desconto de 10% e ficara no valor de {total}')
elif opção == 2:
    total = preço - (preço * 5) / 100
    print(f'sua compra no valor de {preço} terá desconto de 5% e ficara no valor de {total}')
elif opção == 3:
    total = preço
    print(f'sua compra ficara no valor normal de {total}')
else:
    total = preço + (preço * 20) / 100
    print(f'sua compra no valor de {preço} divido em 3x ou mais terá acrescimo de 20% de juros e ficara {total}')                