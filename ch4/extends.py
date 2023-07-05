# class Parent:
#     def __init__(self) -> None:
#         self.value = "테스트"
#         print("Parent 클래스의 __init__ 호출")

#     def test(self):
#         print("Parent 클래스의 test 호출")


# class Child(Parent):
#     def __init__(self) -> None:
#         super().__init__()
#         print("Child 클래스의 __init__ 호출")


# child = Child()
# child.test()
# print(f"부모의 value = {child.value}")


class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value
        print(f"현재 속도(슈퍼클래스) : {self.speed}")

    def downSpeed(self, value):
        self.speed = self.speed - value


class SeDan(Car):
    seatNum = 0

    def upSpeed(self, value):
        self.speed = self.speed + value
        if self.speed > 150:
            self.speed = 150
        print(f"현재 속도(자식클래스) : {self.speed}")

    def getSeatNum(self):
        return self.seatNum


class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity


sedan1, truck1 = SeDan(), Truck()

sedan1.upSpeed(180)
sedan1.downSpeed(20)
sedan1.seatNum = 5
print(sedan1.getSeatNum())
print(sedan1.speed)

truck1.upSpeed(80)
truck1.downSpeed(10)
truck1.capacity = 100
print(truck1.getCapacity())
