dias = (int(input('Digite quantos dias locados: ')))
km = (float(input('Digite os KM rodados: ')))
total = (dias * 60) + (km * 0.15)

print('\nO total a pagar é de {:.2f}R$'.format(total))
