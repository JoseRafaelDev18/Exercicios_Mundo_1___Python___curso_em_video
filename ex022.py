nome = str(input('Digite seu nome completo: ')).strip()

contagem = len(nome.replace(' ', ''))
dividido = nome.split()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome completo possui {} carateres'.format(contagem))
print('Seu primeiro nome tem {} caracteres'.format(len(dividido[0])))
