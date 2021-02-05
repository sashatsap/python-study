first_number = float(input())
operation = input()
second_number = float(input())

if operation == '/' and second_number == 0:
	print("error")
elif operation == '/':
	print(first_number / second_number)
elif operation == '*':
	print(first_number * second_number)
elif operation == '+':
	print(first_number + second_number)
elif operation == '-':
	print(first_number - second_number)
