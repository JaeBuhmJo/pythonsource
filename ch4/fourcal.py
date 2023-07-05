class FourCal:
    def __init__(self, num1, num2) -> None:
        """
        두개의 변수를 받아 멤버 변수 초기화
        """
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


fourcal1 = FourCal(10, 2)
print(fourcal1.add())
print(fourcal1.sub())
print(fourcal1.mul())
print(fourcal1.div())
