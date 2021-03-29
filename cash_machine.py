import sys

correct_login = 'admin'
correct_password = 'admin'


def replenish_balance(balance, amount):
	balance += amount
	print('success')
	return balance


def print_balance(balance):
	print(f'your balance: {balance}')


def withdraw(balance, amount):
	res = balance - amount
	if res >= 0:
		print('success')
		return res
	else:
		print('fail')
		return balance


def verify_account(login, password):
	if login == correct_login and password == correct_password:
		print('success')
		return True
	else:
		print('fail')
		return False


login = (input('write login '))
password = (input('write password '))
if not verify_account(login, password):
	sys.exit()

current_balance = 0

while True:
	choice = (int(input(
		'want you want\n'
		'1 to replenish balance\n'
		'2 to withdraw cash\n'
		'3 to print balance\n'
		'4 to exit the program\n'
	)))
	if choice == 1:
		amount = float(input('write amount '))
		current_balance = replenish_balance(current_balance, amount)

	if choice == 2:
		amount = float(input('write amount '))
		current_balance = withdraw(current_balance, amount)

	if choice == 3:
		print_balance(current_balance)

	if choice == 4:
		sys.exit()
