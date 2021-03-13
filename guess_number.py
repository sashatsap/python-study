from random import randint

user_number = int(input('enter number: '))

while True:
	random_number = randint(1, 100)
	if random_number == user_number:
		print(f'YOUR NUMBER: {random_number}')
		break
