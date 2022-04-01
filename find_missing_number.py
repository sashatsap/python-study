all_nums = 5
nums = [3, 1, 4, 5]

nums.sort()

for i in range(all_nums - 1):
	if nums[i] != i + 1:
		print(i + 1)
		break
