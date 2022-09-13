price_pencil = 1000
price_pen = 2000

num_pencil = int(input("pensil 개수 입력 : "))
num_pen = int(input("pen 개수 입력 : "))

total_price = price_pencil * num_pencil + price_pen * num_pen

if total_price > 10000:
	total_price = total_price * 0.9
	print("10% 할인되었습니다.")

print("종합 : ", int(total_price), "원")