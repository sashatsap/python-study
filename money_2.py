count_50 = 0
count_25 = 0
count_10 = 0
count_5 = 0
count_2 = 0
count_1 = 0
print("Скільки потрібно розбити")
money = int(input())

while money != 0:
	if money >= 50:
		money = money - 50
		count_50 = count_50 + 1
	elif money >= 25:
		money = money - 25
		count_25 = count_25 + 1
	elif money >= 10:
		money = money - 10
		count_10 = count_10 + 1
	elif money >= 5:
		money = money - 5
		count_5 = count_5 + 1
	elif money >= 2:
		money = money - 2
		count_2 = count_2 + 1
	elif money >= 1:
		money = money - 1
		count_1 = count_1 + 1

print(f"{count_50} - 50\n"
      f"{count_25} - 25\n"
      f"{count_10} - 10\n"
      f"{count_5} - 5\n"
      f"{count_2} - 2\n"
      f"{count_1} - 1")
