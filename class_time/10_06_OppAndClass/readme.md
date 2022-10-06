# 양기주 교수님의 대망의 첫 수업

## 객체 지향 프로그래밍(OOP)
* 객체와 클래스
	* 사람이라는 클래스를 만들어서 '서현'객체와 '유진'객체를 찍어낸다.
* 상속
	* 나는 저 클래스를 가져다 쓸게
	* 다중상속, 오버라이딩
* 상속의 조건
	* 추상 기반 클래스  

## 객체
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

## 메소드

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

## 멤버
![image](https://user-images.githubusercontent.com/77817094/194219222-132dace2-3a2c-4553-8f01-782d86f40a91.png)

**퍼블리(Public) 멤버**   
안과 밖 모두에서 접근이 가능한 멤버  

**프라이빗(Private) 멤버**   
클래스 내부(코드 블록 안)에서만 접근이 가능한 멤버  
명명 규칙
* 두 개의 밑줄 __ 이 접두사여야 한다. 예) __number
* 접미사는 밑줄이 한 개까지만 허용된다. 예) __number_
* ![image](https://user-images.githubusercontent.com/77817094/194219788-393771bd-5980-4d21-8a4b-627faf7ccd74.png)

