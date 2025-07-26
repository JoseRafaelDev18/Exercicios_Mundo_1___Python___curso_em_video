reais = float(input('Digite o valor em R$: '))
dol = reais / 5.57
eur = reais / 6.50

print('Os seus {:.2f}R$, equivalem a {:.2f}U$ (Dólares)'.format(reais, dol))
print('Os seus {:.2f}R$, equivalem a {:.2f}€ (Euros)'.format(reais, eur))
