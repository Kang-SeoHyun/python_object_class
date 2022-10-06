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