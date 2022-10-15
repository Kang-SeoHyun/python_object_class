f = -3
print(type(f))
print("hi " * 20)

for i in range(3) :
	for k in range(2) :
		print("i는 %d고, k는 %d다." % (i, k) + '123', 123)
		#이건 안됨.
		# print("i는 %d고, k는 %d다." % (i, k), 123 + '123')