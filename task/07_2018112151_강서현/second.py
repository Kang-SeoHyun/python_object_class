file = open('./task/07_2018112151_강서현/file.txt', 'r', encoding='UTF8')
line = file.readline()
line_num = 1
while line:
	if line_num % 2 == 0:
		x = line[2:6]
		if (int)(x) >= 2020:
			print (line)
	line = file.readline()
	line_num += 1

file.close()