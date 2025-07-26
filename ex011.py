largura = float(input('Digite a largura da sua parade: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura
tinta = area / 2

print('A área da sua parede em metros quadrados é {:.2f}m2!'.format(area))
print('A quantidade de tinta necessária para pintar sua parede de {:.2f}m2 é {:.2f}L!'.format(area, tinta))
