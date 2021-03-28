address = {
	'Іван': '0671234567',
	'Петро': '0669876543',
	'Андрій': '0501111111',
}


def print_dict():
	for name, number in address.items():
		print(f'{name} - {number}')
	print()


def search_by_number(number_choice):
	for name, number in address.items():
		if number == number_choice:
			print(f'{name} - {number}')


def search_by_name(name_choice):
	print(f'{name_choice} - {address[name_choice]}')


def change_name(name_choice, new_name):
	for name, number in address.items():
		if name == name_choice:
			address.pop(name)
			address[new_name] = number
			break


def remove_number(del_name):
	address.pop(del_name)


def add_contact(new_name, new_number):
	address[new_name] = new_number


def change_number(name_choice, new_number):
	address[name_choice] = new_number


while True:
	choice = input(
		'write what you want: \n'
		'1 to all address\n'
		'2 to search by number\n'
		'3 to search by name\n'
		'4 to change name\n'
		'5 to change number\n'
		'6 to remove contact\n'
		'7 to add contact\n'
		'8 to stop\n'
	)

	if choice == '1':
		print_dict()

	if choice == '2':
		search_by_number(input('input number: '))

	if choice == '3':
		search_by_name(input('input name: '))

	if choice == '4':
		old_name = input('what name would you want to rename: ')
		set_name = input('what name do you want: ')
		change_name(old_name, set_name)
		print_dict()

	if choice == '5':
		searching_name = input('whom number do you want to rename: ')
		set_number = input('write new number: ')
		change_number(searching_name, set_number)
		print_dict()

	if choice == '6':
		remove_number(input('what name do you want to remove: '))
		print_dict()

	if choice == '7':
		set_name = input('what name do you want to add ')
		set_number = input('what number do you want to add ')
		add_contact(set_name, set_number)
		print_dict()

	if choice == '8':
		break
