print('Esse é um programa que calcula a média do aluno!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digte a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Você tirou {media}, foi REPROVADO, estude mais!')
elif media >= 7:
    print(f' Você tirou média {media}, Parabéns você foi APROVADO!')    
elif media > 5 or 6.9:
    print(f'Você tirou média {media}, está de RECUPERAÇÃO!')