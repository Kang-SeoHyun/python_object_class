def read_file(input):
	data=[]
	with open(input, 'r', encoding = "utf-8") as file:
		while True:
			line = file.readline().split()
			if not line:
				break
			data.append(line)

	return data

class course:
	def __init__(self, data):
		self.cour_info= []
		self.cour_info = data
	def find_cour(self, input):
		for i in self.cour_info:
			if i[0] == input:
				return i

class professor:
	def __init__(self, data):
		self.pro_info= []
		self.pro_info = data
	def find_pro(self, input):
		for i in self.pro_info:
			for j in i:
				if j == input:
					return i

class student:
	def __init__(self, data):
		self.stu_info= []
		self.stu_info = data
		self.stu_list = []
	def find_stu(self, input):
		for i in self.stu_info:
			for j in i:
				if j == input:
					self.stu_list.append([i[0],i[1],i[2]])

		return self.stu_list

input_class = input("강좌명 입력하쇼: ")

pro_data = read_file("professor.txt")
cour_data = read_file("course.txt")
stu_data = read_file("students.txt")

pro_obj = professor(pro_data)
cour_obj = course(cour_data)
stu_obj = student(stu_data)

get_pro = pro_obj.find_pro(input_class)
get_cour = cour_obj.find_cour(input_class)
get_stu = stu_obj.find_stu(input_class)

print("강좌명	{}\n{}	{}학점".format(get_cour[0], get_cour[1], get_cour[2]))
print("담당교수\n{}	{}".format(get_pro[0], get_pro[1]))
print("수강신청 학생 리스트")
for i in range(len(get_stu)):
    print("{}. {} {} {}".format(i+1, get_stu[i][0], get_stu[i][1], get_stu[i][2]))