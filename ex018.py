from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo: '))

angulo_rad = radians(angulo)

seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print('O seno do ângulo {} é {:.2f}'.format(angulo, seno))
print('O cosseno do ângulo {} é {:.2f}'.format(angulo, cosseno))
print('A tangente do ângulo {} é {:.2f}'.format(angulo, tangente))
