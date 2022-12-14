# 💎파이썬에 대해💎
* 파이썬은 인터프리터 언어  
* 코드가 길어지고 복잡해지면 인터프리트 모드는 번거롭다.  
	* 따라서 스크립트 모드(소스파일 만들어서 전체 실행 하는 것)로 바꿈.

## **✨🧨인터프리터 컴파일러 차이🧨✨**
``` 
컴파일러는 소스코드 전체를 CPU가 읽을 수 있는 기계어롤 변환한다. 
반면, 인터프리터는 소스코드 각 행을 기계어로 번역한다.
따라서 오류가 나면 컴파일러는 컴파일 하는 도중에 오류가 나고,
인터프리터는 분속 도중 어느 행에 오류가 발생하면 그것을 알려주고 멈춘다.
```

컴파일 방식:
* c, c++, 파스칼, 에이다
* CPU가 실행할 수 있는 기계 코드로 컴파일되므로 실행속도가 빠르다.
* 개발 환경과 다른 환경(CPU/OS)로 옮기는 경우, 대체로 코드를 그대로 사용 못 함
	* 이식성 낮음.
	* C#, java 등 가상머신 기반의 언어는 이식성 높음.

인터프리트 방식:
* 베이직, 파이썬, 루비, PHP  
* 애플리케이션을 실행 할 때마다 인터프리터가 소스 코드를 기계 코드로 번역하는 절차를 거치므로 실행속도가 느림 
* 인터프리터만 옮기려는 환경을 지원한다면 변경할 필요 없이 코드 실행이 가능하다.

# 💍컴퓨터 구조론💍
![image](https://user-images.githubusercontent.com/77817094/195242606-2f6201a6-bf5b-4649-b479-5f5307560168.png)  
하드웨어는 컴퓨터를 구성하는 기계적 장치이며,
소프트웨어는 하드웨어의 동작을 지시하고 제어하는 명령어의 집합이다.

## 하드웨어
**CPU란❓**  
```중앙 처리 장치```  
컴퓨터 시스템의 논리적 구성요소로 모든 장치의 동작을 제어하고 명령을 실행 하는 장치이다. (사람으로 치면 뇌🧠)  
내부적으로 3가지로 나눌 수 있다.
* 연산을 수행하는 산술논리장치(ALU)  
* 제어 명령을 전달하는 컨트롤 장치(CU)  
* 결과 값을 일시적으로 기억하는 레지스터(Register)
* ![image](https://user-images.githubusercontent.com/77817094/195243357-ab109d4b-4b61-4b64-b107-987ff33e5fc9.png)

**제어장치와 연산장치의 동작 과정**
1. 먼저 제어장치가 기억장치로부터 명령어를 가져옵니다(Fetch).
2. 제어장치는 가져온 명령어를 해독(Decode)합니다.
3. 제어장치는 해독한 명령어에 따라 산술논리장치에 데이터를 옮기고 어떤 연산을 수행할지를 지시합니다.
4. 산술논리장치는 제어장치가 지시한 대로 계산을 수행(Execute)합니다.
5. 그리고 수행한 결과를 기억장치에 다시 저장(Store)합니다.


**Memory란❓**  
주기억장치  
```
CPU의 Register의 용량은 매우 작아서 정보를 저장해 두었다가 필요할 때 읽어 들여 이용할 수 있는 주 기억 장치가 필요하다. 
컴퓨터가 켜지면 운영체제, 사용자 프로그램등이 주 기억 장치의 메모리공간에 올라가게 된다. 
CPU는 주 기억 장치에서 프로그램들의 명령어등을 읽어와 작업을 수행한다. 
대표적으로 ROM과 RAM으로 나누어 짐.
```
ROM  
``` Read Only Memory ```  
* 오직 데이터를 읽기만 가능함.
* 전원이 끊어져도 데이터들이 소멸되지 않는 비휘발성 메모리.  
* 데이터를 저장한 후 반영구적으로 사용 가능.  

RAM  
``` Random Access Memory ```  
* 읽고 쓰기가 가능  
* 응용 프로그램, OS등을 불러와 CPU가 작업할 수 있도록 하는 기억장치
* 전원이 끊어지면 데이터가 전부 지워지는 휘발성 메모리.
	* 따라서 실행하고 있는 파일은 항상 보조기억장치에 저장을 해줘야 함.

**그 밖에**
* CPU와 주기억장치 사이의 속도 차이를 완화시키기 위해 고속 버퍼(임시)메모리로, 캐시메모리가 존재함.
* ![image](https://user-images.githubusercontent.com/77817094/195245620-55d7fbd2-d747-4251-959e-916f633e5da7.png)  
속도가 빠를 수록 크기가 작은 것을 볼 수 있다.

**흐름**  
![image](https://user-images.githubusercontent.com/77817094/195246760-dfdf372b-ba53-4054-953a-f736a53637f0.png)
![image](https://user-images.githubusercontent.com/77817094/195246566-e9d608d5-c791-42b0-9590-2bc0ce556188.png)
```
1. 컴퓨터에 전원이 들어오게 되면 메인 메모리에 운영체제가 올라간다. 이때 모든 운영체제 코드가 올라가는게아니라 시스템이 돌아가기위한 핵심적인 부분이 먼저올라가는데 이부분을 커널이라 한다. 이러한 이유는 모든 코드가 메모리에 올리게되면 자원낭비가 심하기 때문이다.

2. 그 이후에 CPU는 메모리의 운영체제 프로그램들을 읽어 운영체제를 실행한다. 운영체제가 시작되고 다른 프로그램들을 실행시키면 마찬가지로 메인메모리에 올라가게 된다. 

3. 이때 CPU는 메인메모리에 명령어 주소를 레지스터에 저장하는데 이 레지스터 이름은 PC레지스터라 한다. 

4. 그 이후 각각의 프로그램들은 I/O 디바이스 사용이 필요할 수 있는데 이러한 요청은 운영체제한테 해야한다. 이러한 요청을 시스템콜이라고 한다. 이렇게 프로그램들이 직접 I/O디바이스를 제어하지 않는 이유는 많은 이유가있지만 가장 큰 이유는 보안 때문이다.

5. 프로그램의 요청을 받은 운영체제는 I/O 디바이스의 컨트롤러에게 데이터 입출력 처리를 요청을 한다. 그리고 I/O 디바이스 컨 틀롤러들은 입출력을 받게 되면 Interrupt를 발생시켜 CPU에게 작업이 완료됐다고 알리게 된다.

6. CPU는 I/O 디바이스에 버퍼에 가서 데이터를 읽어와 메인 메모리에 올려놓게 된다. 이러한 작업이 반복되는 것이 컴퓨터 프로그램의 동작 원리이다. 
```

# **✨리스트, 튜플, 딕셔너리✨**
> 개 중요함.
## 리스트✏
``` 데이터의 목록을 다루는 자료형 ```  
slot: 리스트의 데이터를 넣을 자리.  
element: 슬롯에 꽂혀있는 개별 데이터.  
리스트 만들 때는 대괄호 사용
* 각 데이터는 콤마로 구분(['a','b','c'] 이런 식)
* '+' 연산자로 리스트 간 결합 가능
* 슬라이싱: [2:5] = 2,3,4 [:4] = 0,1,2,3 [5:] = 5부터 끝까지
* len(리스트) 넣으면 데이터 갯수 나옴
* a[2] = 20으로 데이터 변경 가능  

### **메소드**
+ .append()
	+ 리스트 끝에 새 요소 추가  
+ .extend()
	+ 리스트에 다른 리스트 이어 붙임  
+ .insert()
	+ a.insert(2, 4) 2번 인덱스 위치에 4 집어넣음  
+ .remove()
	+ 매개변수로 입력한 데이터를 찾아서 제거  
	+ a.remove('hello')
+ .pop()
	+ a.pop() 마지막 요소를 뽑아서 제거함.  
	+ a.pop(2) 인덱스 입력해도 제거 됨  
+ .index()
	+ a.index('banana') 매개변수로 들어온 값의 인덱스 위치 찾아줌.  
+ .count()
	+ 매개변수로 입력한 데이터와 일치하는 요소가 몇개인지 셈  
+ .sort()
	+ 오름차순으로 정렬  
	+ .sort(reverse = True) 내림차순으로 정렬  
+ .reverse()
	+ 요소의 순서를 반대로 뒤집음 [안녕요] -> [요녕안]  

## **✨🧨리스트와 튜플의 차이🧨✨**
1. list는 데이터 변경 가능하다.  
	+ list 생성 후 추가, 수정, 삭제 가능.  
2. tuple은 데이터 변경이 불가능하다.  
	+ 튜플 생성 후 추가, 수정, 삭제 불가능.  
3. list는 이름 그대로 목록 형식의 데이터를 다루는 데 적합하다.  
4. tuple은 RGB 색상처럼 작은 규모의 자료구조를 구성하기에 적합하다.  

## 튜플✏
``` N개의 요소로 된 집합 ```  
변경이 불가능한 자료형이 필요한 이유?  
> 데이터를 할당할 공간의 내용이나 크기가 달라지지 않기 때문.  
> 데이터가 오염되지 않을 것이라는 보장이 있어서 원본 사용 가능함.  
> 신뢰가 가능한 코드.  

튜플 만들 때는 ()괄호나 , 사용
* a = (1, 2, 3) or a = 1, 2, 3
	* 요소가 하나면 뒤에 , 추가  
	* a = (1, ) or a = 1,
* '+' 연산자로 튜플 간 결합 가능
* 슬라이싱: [2:5] = 2,3,4 [:4] = 0,1,2,3 [5:] = 5부터 끝까지
* a[2] = 20 이런 식인 데이터 변경 불가능 
* len(리스트) 넣으면 데이터 갯수 나옴  

```python
#튜플생성: 패킹
a = 1, 2, 3 
#튜플 언패킹
one, two, three = a
# 요소의 수와 변수의 갯수가 일치해야 함
```
### **메소드**
+ .index()
	+ a.index('banana') 매개변수로 들어온 값의 인덱스 위치 찾아줌.  
+ .count()
	+ 매개변수로 입력한 데이터와 일치하는 요소가 몇개인지 셈

## 딕셔너리✏  
``` 사용법 측면에선 리스트와 비슷 ```  
리스트는 인덱스(0부터 시작)를 첨자처럼 사용하지만 딕셔너리는 어떤 자료형이든 첨자로 사용 가능하다.
* 딕셔너리의 첨자는 키(key)  
* 이 key가 가리키는 슬롯에 있는 데이터를 value라고 한다.  
* 딕셔너리는 key-value의 쌍으로 구성    
* 탐색 속도가 빠르고, 사용하기 편리  
* 딕셔너리 생성할땐 { } 사용  
* 요소 참조하거나, 새로운 키-벨류 입력할 때 [ ] 사용

```python
 #딕셔너리 생성
student1 = {'이름': '홍길동', '학번': '2018112151'}
#키-벨류 추가
student1['학과'] = '열공학과' 
student1['연락처'] = '010-1111-1111'
```
### **메소드**
+ .get(key)
	+ value 값을 찾아 줌.
	+ key가 없을 때 아무것도 반환 안함.
+ .keys(), .values()
	+ 데이터 뭐가 있는지 알려 줌.
+ .items()
	+ 전체적으로 뭐 있는지 알려 줌.
+ 'apple' in fruits.keys() or .values()
	+ boolean 형식으로 존재 여부 알려줌
+ .pop(key)
	+ 그 키의 요소(키,벨류)를 삭제함.
+ .clear()
	+ 딕셔너리 내용 다 없어짐.
+ for문으로 딕셔너리 모든 값 출력.
	+ ![image](https://user-images.githubusercontent.com/77817094/195982450-1b92f77b-a04b-437b-84f9-c8ff7bcdd660.png)

# 🥽반복문🥽

## while문
``` 코드로 대체 ```  

## for문
``` 코드로 대체 ```   

### range() 함수  
-> range(시작값, 멈춤값, 연속하는 두 수의 차)

## if문
``` 코드로 대체 ``` 

# 🎁모듈과 패키지🎁
## 모듈🧀
``` 파이썬에서는 개별 소스 파일을 일컫는 말 ```   
* 모듈 : 독자적인 기능을 갖는 구성 요소  
* 표준 모듈 : 파이썬과 함께 따라오는 모듈  
* 사용자 생성 모듈 : 프로그래머가 직접 작성한 모듈  
* 서드 파티 모듈 : 업체 또는 다른 프로그래머에서 제공한 모듈  


**import의 역할**  
``` 두 개의 소스 파일(모듈)로 하나의 프로그램 만들기 ```  
* 다른 모듈 내의 코드에 대한 접근을 가능하게 함  
* 다른 코드에는 함수, 클래스 등이 포함되어 있음.
* 사용법: 
	* import calculator  
	* from calculator import plus
	* 코드로 대체  

**메인 모듈**  
``` 최상위 수준으로 실행되는 스크립트 ```  
__name__ : __main__ 으로 뜸.

## 패키지🧀  
``` 모듈 꾸러미 ```
* 모듈을 모아놓는 디렉토리
* 디렉토리가 "파이썬의 패키지"로 인정받으려면 __init__.py 파일을 그 경로에 갖고 있어야 함.  
	* 보통의 경우 init__.py 파일은 대개 비워둠 

# 🍟오류 다루기🍟  

**예외란?**  
문법적으로 문제가 없는 코드를 실행할 때 발생하는 오류  
> value error등

**try ~ except로 예외 처리하기**  
```python
try:
	# 문제 없을 때 실행 할 코드
except:
	# 문제 발생시 실행 할 코드
```
**복수 개의 except로 예외 처리하기**  
```python
try:
	# 문제 없을 때 실행 할 코드
except 예외형식1:
	# 문제 발생시 실행 할 코드
except 예외형식2:
	# 문제 발생시 실행 할 코드
```
> 예외형식: 파이썬이 제공하는 내장 예외 형식  

**예외의 인스턴스 활용하기 - as 문 사용**  
```python
try:
	# 문제 없을 때 실행 할 코드
except 예외형식1 as err:
	# 문제 발생시 실행 할 코드
except 예외형식2 as err:
	# 문제 발생시 실행 할 코드
```
**except절에 대한 else**
```python
try:
	# 문제 없을 때 실행 할 코드
except:
	# 문제 발생시 실행 할 코드
else:
	# except절을 만나지 않았을 경우 실행 할 코드
```
**항상 발생하는 finally 코드**
```python
try:
	# 문제 없을 때 실행 할 코드
except:
	# 문제 발생시 실행 할 코드
finally:
	# 항상 마지막에 실행 되는 코드
```

내장 예외 형식만으로 충분하지 않을 때 직접 예외 클래스를 정의할 수 있음.  
```python
class MyException(Exception):
	def __init__(self):
		super().__init__("내 예외가 발생했습니다.")
```

# 🍺파일 데이터 관리🍺
``` 열고 읽고 쓰고 닫고 ```  
![image](https://user-images.githubusercontent.com/77817094/196021703-9b190730-2ac6-4d1e-a503-557290e877d3.png)

**자원 누수 방지**  
with ~ as 문을 사용하면 close() 함수를 사용하지 않아도 됨.
```python
with open('./middle/Ex11/test.txt', 'r') as file:
	str = file.read()
	print(Str)
	#file.close()
```

**open( )함수**  
하나의 필수 매개변수와 일곱 개의 매개변수  
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, 
newline=None, closefd=True, opener=None) 
```  
파일 열기 모드  
![image](https://user-images.githubusercontent.com/77817094/196023068-ab2ea687-b6a5-4f89-945b-ed3253437b62.png)

## 인코딩🍑
***아스키코드***
* American Standard Code for Information Interchange  
* 미국 정보 교환 표준 부호, 총 128개의 문자  
* A ~ Z = 65 ~ 90, a ~ z = 97 ~ 122, 마지막: 127번  

***DBCS***
* 최대 65536(2^16)개의 문자 사용 가능
* 한글, 중국, 일본 문자 표현 가능
* 아스키와의 호환을 유지하기 위해 최상위 비트를 1로 함 (아스키는 0)  

***유니코드***
* 문자 집합 하나로 모든 문자를 표현할 수 있게 하는 것이 목적
* 문자에 부여되는 번호를 코드 포인트라고 함.
	* 코드포인트는 “U+” 뒤에 2바이트의 수를 16진수로 표현하여 붙여 표시
		* ex: 'A'의 코드 포인트는 U+0041

***UTF***
* Unicode Transformation Format
* 유니코드 변환 인코딩 형식
* UTF-8 외에도 UTF-7, UTF-16, UTF-32 인코딩 등이 있음.
* UTF-8은 코드포인트의 크기에 따라 1바이트에서부터 4바이트까지 가변폭으로 인코딩하므로 1 바이트로 표현 가능한 U+0000(십진수 0)부터 U+007F(십진수 127)까지는 ASCII와 완벽하게 호환

# 🍳객체지향과 클래스🍳

## 객체 지향 프로그래밍(OOP)👚
* 객체와 클래스
	* 사람이라는 클래스를 만들어서 '서현'객체와 '유진'객체를 찍어낸다.
* 상속
	* 나는 저 클래스를 가져다 쓸게
	* 다중상속, 오버라이딩
* 상속의 조건
	* 추상 기반 클래스  

## 객체(object)👚
``` 객체(object) = 속성(attribute) + 기능(method) ```

**속성?**  
자동차의 속성 : 색, 바퀴 크기, 엔진 배기량  
**기능?**  
자동차의 기능 : 전진, 후진, 좌회전, 우회전  
**속성 + 기능?**  
자동차 객체 : 16인치의 바퀴를 가진 2000cc의 빨간 차는 전진, 후진, 좌회전, 우회전의 기능이 있다.  

```python
class Car:
    def __init__(self): #__init__ 은 초기화하는 함수
        self.color = 0xFF0000    # 바디의 색
        self.wheel_size = 16     # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량
	
    def forward(self): # 전진
        pass

    def backward(self): # 후진
        pass

    def turn_left(self): # 좌회전
        pass

    def turn_right(self): # 우회전
        pass

```
## 클래스(class)👚
```python
class 클래스이름:
	코드블록(변수와 메소드로 이루어짐.)
```  
``` 함수와 거의 동일한 의미지만 메소드는 클래스의 멤버라는 점이 다르다. ```  

## 메소드(method)👚
**인스턴스 메소드**  
* 인스턴스(객체)에 속한 메소드
	* 인스턴스 메소드가 “인스턴스에 속한다”라는 표현은 “인스턴스를 통해 호출가능하다.” 라는 뜻

**정적 메소드**
* 클래스에 귀속
* @staticmethod 데코레이터로 수식
* self 키워드 없이 정의
* ```python 
	class 클래스이름:
    @staticmethod
    def 메소드이름( 매개변수 ): #self매개변수 사용X
        pass
	```

**클래스 메소드**
* 클래스에 귀속  
* @classmethod 데코레이터로 수식  
* cls 매개변수 사용
* ```python
	class 클래스이름:
    # ...
    
    @classmethod
    def 메소드이름(cls): #매개변수 하나이상
        pass
	```
* ![image](https://user-images.githubusercontent.com/77817094/194218746-f5138188-e027-4225-b38e-dc36f48c6d01.png)

## 👚멤버(member)👚
![image](https://user-images.githubusercontent.com/77817094/194219222-132dace2-3a2c-4553-8f01-782d86f40a91.png)

**퍼블리(Public) 멤버**   
안과 밖 모두에서 접근이 가능한 멤버  

**프라이빗(Private) 멤버**   
클래스 내부(코드 블록 안)에서만 접근이 가능한 멤버  
명명 규칙
* 두 개의 밑줄 __ 이 접두사여야 한다. 예) __number
* 접미사는 밑줄이 한 개까지만 허용된다. 예) __number_
* ![image](https://user-images.githubusercontent.com/77817094/194219788-393771bd-5980-4d21-8a4b-627faf7ccd74.png)

## 👚상속(Inheritance)👚

**상속?**  
한 클래스가 다른 클래스로부터 데이터 속성과 메소드를 물려받는 것.

![image](https://user-images.githubusercontent.com/77817094/194220764-2d793649-a479-4aee-a4ee-3819f7c341bf.png)

```python
class Base:
	def base_method(self):
		print("base_method")

		
class Derived(Base):
	pass

base = Base()
base.base_method()
derived = Derived()
derived.base_method()

#출력 결과
#base_method
#base_method
```

**super()**
``` 08번 과제, bank 코드로 대체 ```

**다중상속**  
```python
class A:
	pass
class B:
	pass
class C:
	pass
class D(A, B, C):
	pass

#D는 여러 부모로부터 상속을 받았다 -> 다중상속
```

**오버라이딩**  
```python
class A:
	def method(self, a, b):
		print(a + b)

class B(A):
	def method(self, a, b):
		print(a + b - a * b)

class C(B):
	def method(self, a, b):
		print(a * b * (a - b))

A().method(2,3) # 5
B().method(2,3) # -1
C().method(2,3) # -6
```