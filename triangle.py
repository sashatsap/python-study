first_triangle = []
second_triangle = []
for i in range(1, 4):
	x = int(input(f'write the {i} side :  '))
	first_triangle.append(x)
	x = 0

for u in range(1, 4):
	z = int(input(f'write the {u} side :  '))
	second_triangle.append(z)
	z = 0

res_1 = first_triangle[0] / second_triangle[0]
res_2 = first_triangle[1] / second_triangle[1]
res_3 = first_triangle[2] / second_triangle[2]
if res_1 == res_2 and res_2 == res_3:
	print('ok')
else:
	print('no')