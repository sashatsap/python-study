answer = 0
count = 0
s = input('Enter string: ')
check = []
for i in range(len(s)):
    if s[i] not in check:
        check.append(s[i])
        count += 1
    else:
        if count > answer:
            answer = count
            count = 1


print(answer)