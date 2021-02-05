print("введіть число")
x = int(input())

print("введіть степінь")
n = int(input())

res = 1

for i in range(n):
	res = res * x

print(res)
