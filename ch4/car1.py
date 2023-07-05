# class Car:
#     color = ""
#     speed = 0

#     def upSpeed(self, value):
#         self.speed += value


#     def downSpeed(self, value):
#         self.speed -= value


class Car:
    def __init__(self) -> None:
        self.color = ""
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


car1 = Car()
car1.color = "Red"
car2 = Car()
car2.color = "Blue"
car3 = Car()
car3.color = "Yellow"

# 첫번째 자동차 색상은 Red이며, 현재속도는 50km입니다
car1.upSpeed(100)
print("첫번째 자동차 색상은 %s이며, 현재속도는 %dkm입니다." % (car1.color, car1.speed))

car2.upSpeed(60)
car2.downSpeed(20)
print("두번째 자동차 색상은 {}이며, 현재속도는 {}km입니다.".format(car2.color, car2.speed))

car3.upSpeed(150)
car3.downSpeed(50)
print(f"세번째 자동차 색상은 {car3.color}이며, 현재속도는 {car3.speed}km입니다.")
