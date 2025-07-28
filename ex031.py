km = int(input('Qual a distância da viagem? '))

if km <= 200:
    print(f'O total da passagem é {km * 0.5}R$')
else:
    print(f'O total da passagem é {km * 0.45}R$')
