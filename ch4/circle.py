import math


class Circle:
    def __init__(self, radius) -> None:
        """
        __변수명 : private
        """
        self.__radius = radius

    def getCircum(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * (self.__radius**2)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius


circle = Circle(10)
# print(circle.__radius)  # 접근 불가
print(circle.getRadius())
circle.setRadius(8)
print(circle.getRadius())
print(circle.getArea())
