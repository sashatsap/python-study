first_triangle = []
second_triangle = []

for i in range(3):
	x = int(input(f'enter the length of {i + 1} side: '))
	first_triangle.append(x)

for i in range(3):
	x = int(input(f'enter the length of {i + 1} side: '))
	second_triangle.append(x)

res_1 = first_triangle[0] / second_triangle[0]
res_2 = first_triangle[1] / second_triangle[1]
res_3 = first_triangle[2] / second_triangle[2]

if res_1 == res_2 == res_3:
	print('ok')
else:
	print('no')
