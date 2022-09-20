print("정수를 입력하라")
a = int(input())
re_list = []

for i in range(2,a):
    count = 0
    
    for k in range(1, i+1):
        if i % k == 0:
            count += 1
    if count <= 2:
        re_list.append(i)

if (len(re_list) % 2):
	for i in range(len(re_list)):
		re_list[i] = re_list[i] + 1
	print (re_list)
else:
	print (re_list)
