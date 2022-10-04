file = open('./task/07_2018112151_강서현/file.txt', 'r', encoding='UTF8')

line = file.readline()
line_num = 1
new_file = ""
while line:
	if line_num % 2 == 0:
		x = line[14:17]
		if x == '명진관':
			line = line.replace('명진관', '과학관')
		elif x == '과학관':
			line = line.replace('과학관', '명진관')
	new_file = new_file + line
	line = file.readline()
	line_num += 1

file = open('./task/07_2018112151_강서현/file1.txt', 'w', encoding='UTF8')
file.write(new_file)
file.close()