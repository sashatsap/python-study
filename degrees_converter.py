x = input('f (fahrenheit -> celsius) or c (celsius -> fahrenheit): ')
degree = int(input('print degree: '))

if x == 'f':
	print(f'res = {(degree - 32) / 1.8}')
else:
	print(f'res = {degree * 1.8 + 32}')
