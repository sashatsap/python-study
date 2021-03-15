numbers = [4, -5, 1, 9]

for i in range(len(numbers)):
	if numbers[i] % 2 == 1:
		numbers[i] = 1
	else:
		numbers[i] = 0

print(numbers)
