all_nums = 5
nums = [3, 1, 4, 5]

for i in range(len(nums)):
	for j in range(len(nums)):
		if nums[i] < nums[j]:
			temp = nums[j]
			nums[j] = nums[i]
			nums[i] = temp

for i in range(all_nums - 1):
	if nums[i] != i + 1:
		print(i + 1)
		break
