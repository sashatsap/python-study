"""
Число 1 є менше, ніж 5
Число 0 є менше, ніж 5
"""

numbers = [1, 0, 5, 4, 9]

for number in numbers:
	if number < 5:
		print(f"число {number} є менше, ніж 5")
	elif number > 5:
		print(f"число {number} є більше, ніж 5")
	else:
		print(f"число {number} є рівне 5")
