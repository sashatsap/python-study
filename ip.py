print('Введіть ip')
make_ip = input()
is_valid = True

for ip_elem in make_ip.split('.'):
	if int(ip_elem) > 255 or int(ip_elem) < 0:
		is_valid = False
		break

if is_valid:
	print('Okay')
else:
	print('error')
