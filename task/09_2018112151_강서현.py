class A:
	def method(self, a, b):
		print(a + b)

class B(A):
	def method(self, a, b):
		print(a + b - a * b)

class C(B):
	def method(self, a, b):
		print(a * b * (a - b))

A().method(2,3)
B().method(2,3)
C().method(2,3)