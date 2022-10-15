#아예 소스파일로 가능
import calculator

#소스파일의 기능으로도 가능
from calculator import plus

#연달아 말하기 가능
from calculator import plus, minus

#와일드카드(*) 사용 가능
from calculator import *

#별칭만들기 가능
import calculator as c

# 내장되어 있는 모듈의 목록 볼 수 있음.
import sys 
print(sys.builtin_module_names)