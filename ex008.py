metros = float(input('Digite o valor que deseja converter, em metros: '))
km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('{}m equivalem a {:.3f}km'.format(metros, km))
print('{}m equivalem a {:.3f}hm'.format(metros, hm))
print('{}m equivalem a {:.3f}dam'.format(metros, dam))
print('{}m equivalem a {:.3f}dm'.format(metros, dm))
print('{}m equivalem a {:.3f}cm'.format(metros, cm))
print('{}m equivalem a {:.3f}mm'.format(metros, mm))
