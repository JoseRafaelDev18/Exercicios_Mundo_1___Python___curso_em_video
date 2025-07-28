salario = float(input('Digite seu salário atual: '))

if salario > 1250.00:
    print('Seu novo salário é {:.2f}!'.format(salario * 1.10))
else:
    print('Seu novo salário é {:.2f}!'.format(salario * 1.15))
