nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
diagonals_sum = [0, 0]
columns_sum = [0 for _ in range(len(nums[0]))]
lines_sum = []
table_sum = 0

for i in range(len(nums)):
	for j in range(len(nums[0])):
		table_sum += nums[i][j]

for i in range(len(nums)):
	line_sum = 0
	for j in range(len(nums[0])):
		line_sum += nums[i][j]
	lines_sum.append(line_sum)

for i in range(len(nums)):
	for j in range(len(nums[0])):
		columns_sum[j] += nums[i][j]

for i in range(len(nums)):
	diagonals_sum[0] += nums[i][i]

for i in range(len(nums)):
	diagonals_sum[1] += nums[i][len(nums) - i - 1]

print(f'sum of columns: {columns_sum}')
print(f'sum of lines: {lines_sum}')
print(f'sum of diagonals: {diagonals_sum}')
print(f'sum of table: {table_sum}')
