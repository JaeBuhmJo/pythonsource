class Calc:
    """
    생성자 작성 - 멤버 변수 result
    """

    def __init__(self, result) -> None:
        self.result = result

    def adder(self, num):
        self.result += num
        return self.result


calc1 = Calc(7)
print(calc1.adder(3))
