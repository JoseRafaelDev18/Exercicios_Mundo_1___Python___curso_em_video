from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
'''hipo = (oposto ** 2 + adjacente ** 2) ** (1/2)

print('O valor da Hipotenusa é {:.2f}!'.format(hipo))'''

hipo = hypot(oposto ,adjacente)

print('O valor da hipotenusa é {:.2f}!'.format(hipo))
