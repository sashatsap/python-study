res = 0
elements = []
elem_num = int(input('how many elements do you want to input: '))

for _ in range(elem_num):
	num = int(input('input number:'))
	elements.append(num)

for i in range(elem_num):
	res += elements[i]

print(res)
