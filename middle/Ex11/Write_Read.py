lines = ["we'll find a way we always have - Interstellar\n", 
         "I'll find you and I'll kill you - Taken\n",
         "I'll be back - Terminator 2\n"]

with open('./middle/Ex11/movie_quotes.txt', 'w') as file:
    for line in lines:
        file.write(line)

print('한줄 넣기')
with open('./middle/Ex11/movie_quotes.txt', 'r') as file:
	line = file.readline()

	while line != '':
		print(line)
		line = file.readline()

print('list에 줄 별로 다 넣기')
with open('./middle/Ex11/movie_quotes.txt', 'r') as file:
	line_list = file.readlines()
	print(type(line_list))

	for line in line_list:
		print(line)