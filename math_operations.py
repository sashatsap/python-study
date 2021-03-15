the_smallest_num = 10 ** 10
the_biggest_num = -10 ** 10
sum_of_negative_elms = 0
product_between_min_and_max = 0
product_between_all_even_numbers = 1
num = [3, 7, -2, 10, 6, -5, 1]

for i in range(len(num)):
	if num[i] < 0:
		sum_of_negative_elms += num[i]

for i in range(len(num)):
	if num[i] < the_smallest_num:
		the_smallest_num = num[i]

for i in range(len(num)):
	if num[i] > the_biggest_num:
		the_biggest_num = num[i]

product_between_min_and_max = the_smallest_num * the_biggest_num

for i in range(len(num)):
	if num[i] % 2 == 0:
		product_between_all_even_numbers *= num[i]

print(f'sum of negative elements: {sum_of_negative_elms}')
print(f'product between min and max: {product_between_min_and_max}')
print(f'product between all even numbers: {product_between_all_even_numbers}')
