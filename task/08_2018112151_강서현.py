class Account:
	def __init__(self, accountNum, balance):
		self.accountNum = accountNum
		self.balance = int(balance)

	def deposit(self, inputMoney):
		self.balance += int(inputMoney)
		print(inputMoney + "원 입금하셨습니다.")
		print("현재 잔액은 " + str(self.balance) + "원 입니다.")

	def withdraw(self, outputMoney):
		self.balance -= int(outputMoney)
		if self.balance < 0:
			print(outputMoney + "원을 출금하려 하였으나, 돈이 부족하여 실패했습니다.")
			self.balance += int(outputMoney)
			print("현재 잔액은 " + str(self.balance) + "원 입니다.")
		else :
			print(outputMoney + "원 출금하셨습니다.")
			print("현재 잔액은 " + str(self.balance) + "원 입니다.")

class Customer(Account):
	def __init__(self, name, phoneNum, account):
		self.name = name
		self.phoneNum = phoneNum
		#self.account = account
		super().__init__(account.accountNum, account.balance)


if __name__ == '__main__':
	a_acunt = Account('835002-04-222604', 30000)
	A = Customer('seohyun', '010-5291-6615', a_acunt)
	b_acunt = Account('110-486-867100', 2000)
	B = Customer('youjin', '010-9809-6826', b_acunt)
	
	A.deposit('8000')
	A.withdraw('12000')
	print("현재 " + A.name + "님 통장엔" + str(A.balance) + "원 있습니다.")

	B.deposit('100')
	B.withdraw('32000')
	print("현재" + B.name + "님 통장엔 " + str(B.balance) + "원 있습니다.")