def read_file(input):
	with open(input, 'r', encoding = 'utf-8') as file:
		data = []
		while True:
			line = file.readline().split()
			if not line:
				break
			data.append(line)

		return data

class course:
	def __init__(self, data):
		self.data = []
		self.data = data
	def find_info(self, major):
		for i in self.data:
			if i[0] == major:
				return i

class professor:
	def __init__(self, data):
		self.data = []
		self.data = data
	def find_info(self, major):
		for i in self.data:
			for j in i:
				if j == major:
					return i

class student:
	def __init__(self, data):
		self.data = []
		self.data = data
		self.info = []
	def find_info(self, major):
		for i in self.data:
			for j in i:
				if j == major:
					self.info.append([i[0], i[1], i[2]])

		return self.info



cour_data = read_file("./middle/2021_middle/course.txt")
stu_data = read_file("./middle/2021_middle/students.txt")
pro_data = read_file("./middle/2021_middle/professor.txt")

cour_obj = course(cour_data)
pro_obj = professor(pro_data)
stu_obj = student(stu_data)

major = input("강좌명을 입력하세요: ")

print (cour_obj.find_info(major)[0], )
print (pro_obj.find_info(major))
print (stu_obj.find_info(major))