from random import randint
from time import sleep

print('===-==='*5)
print('Bem vindo ao meu programa!')
print('===-==='*5)
sleep(1)

escolha = int(input('\nDigite um número: '))
escolhido = randint(1, 5)

print('\nProcessando...')
sleep(2)

if escolhido == escolha:
    print('\nParabéns, você venceu!')
else:
    print('\nVocê errou! A máquina venceu.')
