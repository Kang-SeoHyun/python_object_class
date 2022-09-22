def jjik_make(a):
	for n in range(0, a) :
		print("____", end='')

def chat_bot(n, a):
	if n == 0 :
		jjik_make(a - n)
		print("\"재귀함수가 뭔가요?\"")
		jjik_make(a - n)
		print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
	else :
		jjik_make(a - n)
		print("\"재귀함수가 뭔가요?\"")
		jjik_make(a - n)
		print("\"잘 들어봐. 어려운 문제는 어떻게 하라고 했지? 인터넷을 검색하면 정답이 나온다고\"")
		chat_bot(n - 1, a)
	jjik_make(a - n)
	print("라고 답변하였지.", end='')
	if (a - n != 0) :
		print("")

n = int(input())
print("어느 한 정보통신공학과 학생이 객체시간에 질문이 나왔다.")
chat_bot(n, n)
