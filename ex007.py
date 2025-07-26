nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('\nSua primerira nota foi {:.2f}'.format(nota1))
print('\nSua segunda nota foi {:.2f}'.format(nota2))
print('\nSua terceira nota foi {:.2f}'.format(nota3))
print('\nSua quarta nota foi {:.2f}'.format(nota4))
print('\nSua média é {:.2f}'.format(media))

if(media >= 7):
    print('\nVocê está aprovado(a)!')
elif(media >= 4):
    print('\nVocê está em recuperação!')
else:
    print('\nVocê está reprovado(a)!')
