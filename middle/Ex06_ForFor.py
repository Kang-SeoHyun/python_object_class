for i in range(1, 10):
	for j in range(i):
		if i % 2 == 1:
			continue #제일 가까운 반복문으로 다시 돌아감!
		print( "*", end = "")

	print()
#break 는 반복문 중단함