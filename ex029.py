vel = int(input('A quantos KM/h o veículo está? '))
if vel > 80:
    print(f'Você exceceu o limite de velocidade de 80KM/h! O valor da multa é {(vel - 80) * 7}R$.')
else:
    print('Você está dentro do limite de velocidade, parabéns!')
