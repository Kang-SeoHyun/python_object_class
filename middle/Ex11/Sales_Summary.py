salesfile = open('./middle/Ex11/sales.txt', 'r')
sales = salesfile.readlines()
sum = 0
count = 0
for price in sales:
	sum += int(price)
	count += 1

summaryfile = open('./middle/Ex11/summary.txt', 'w', encoding = 'utf-8')
summaryfile.write("총 매출 = " + str(sum))
summaryfile.write("\n평균 일매출 = " + str(sum / count))
