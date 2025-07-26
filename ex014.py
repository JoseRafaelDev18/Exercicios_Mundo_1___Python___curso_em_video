tempc = float(input('Digite a temperatura (em °C:): '))
tempf = tempc * 9 / 5 + 32
tempk = tempc + 273.15

print('{}°C equivalem a {:.1f}°F (Fahrenheits)'.format(tempc, tempf))
print('{}°C equivalem a {:.1f}K (Kelvins)'.format(tempc, tempk))
