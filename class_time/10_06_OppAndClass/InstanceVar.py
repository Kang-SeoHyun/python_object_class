class InstanceVar:
	def __init__(self): #초기화해줘서 다시 만들어지면 이전내용 없어짐
		self.text_list = []

	def add(self, text):
		self.text_list.append(text)

	def print_list(self):
		print(self.text_list)

if __name__ == '__main__':
	list = InstanceVar()
	list.add('a')
	list.print_list()
	list.add('b')
	list.print_list()

	list2 = InstanceVar()
	list2.add('a')
	list.print_list()
