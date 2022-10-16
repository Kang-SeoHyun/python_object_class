lines = ['안녕하세요?\n', 'こんにちは\n', 'Hello.\n']

with open ('./middle/Ex11/utf8.txt', 'w', encoding ='utf-8') as file:
	for line in lines:
		file.write(line)

with open ('./middle/Ex11/utf8.txt', 'w', encoding ='ascii') as file:
	for line in lines:
		file.write(line)

with open ('./middle/Ex11/utf8.txt', 'w', encoding ='ascii', errors='ignore') as file:
	for line in lines:
		file.write(line)