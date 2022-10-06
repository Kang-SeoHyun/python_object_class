class Car:
    def __init__(self):
        self.color = 0xFF0000    # 바디의 색
        self.wheel_size = 16     # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량

    def forward(self): # 전진
        print("전진 중 입니다.")

    def backward(self): # 후진
        print("후진 중 입니다.")

    def turn_left(self): # 좌회전
        print("좌회전 합니다.")

    def turn_right(self): # 우회전
        print("우회전 합니다.")

#Car 클래스 정의 종료. 아래는 Car 클래스의 인스턴스를 정의하고 사용하는 코드

if __name__ == '__main__':        
    my_car = Car()

    print('0x{:02X}'.format(my_car.color))
	#print(my_car.color)
    print(my_car.wheel_size)
    print(my_car.displacement)

    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()
