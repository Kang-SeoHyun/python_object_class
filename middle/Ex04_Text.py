a = 'hello'
b = "world"
c = a + ', ' + b
print(c)

print(c[0:4]) # 0에서 4앞까지
print('Good' in c)
print('world' in c)
print(len(c)) #strlen

c.find("ll") # 있는 곳 인덱스 찾아줌! 없으면 -1반환
c.rfind('rl') # 뒤에서부터 있는 곳 인덱스 찾아줌
c.count('l') # 몇번 등장하는지

"    hello".lstrip() #왼쪽 공백 없애줌
"hello    ".rstrip() #오른쪽 공백 없애줌
"    hello    ".strip() #양쪽 공백 없애줌

" ".isalpha() # 오직 알파벳
" ".isnumeric() # 오직 숫자
" ".isalnum() # 오직 알파벳과 수
" ".upper() # 대문자로
" ".lower() # 소문자로

d = c.replace('o', 'ow')
print(d)

fruits = "apple, kiwi, banana"
fruits_list = fruits.split(", ")
print(fruits_list)
print(type(fruits_list))
