class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':
	kang = ContactInfo('강서현', 'jiye_kang@naver.com')
	lee = ContactInfo('이유진', 'a98yjlee@naver.com')

	kang.print_info()
	lee.print_info()