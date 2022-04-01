all_nums = 5
nums = [3, 1, 4, 5]

for i in range(all_nums):
	was_found = False
	for j in range(len(nums)):
		if nums[j] == i + 1:
			was_found = True

	if was_found == False:
		print(i + 1)
		break
