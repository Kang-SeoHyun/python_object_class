input_list = list(map(int, input().split()))

for num in input_list:
	if num < 0:
		print ("!!!error!!!")
		quit()
	if num > 2147483647:
		print ("!!!error!!!")
		quit()

def is_squrt(n):
    s = n ** 0.5

    if s == int(s):
        answer = s
    else:
        answer = -1

    return int(answer)

def circle_area(n):
	return n * n * 3.14

def cube_volume(n):
	return n * n * n

for num in input_list:
	result_list = list([is_squrt(num), circle_area(num), cube_volume(num)])
	print (result_list)