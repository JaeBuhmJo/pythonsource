# class Student(): 상속이 이뤄질 경우는 ()안에 부모 클래스를 써야 함
class Student:
    def __init__(self, name, number, grade, details) -> None:
        """
        생성자(오버로딩 없음)
        """
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    def __str__(self) -> str:
        """
        toString 역할
        """
        return "이름 : {} 학년 : {} 반 : {} 학생정보 : {}".format(
            self.name,
            self.grade,
            self.number,
            self.details,
        )


# 객체 생성
student1 = Student(
    "Kim",
    1,
    1,
    {"gender": "male", "score1": 95, "score2": 99},
)
student2 = Student(
    "Park",
    2,
    2,
    {"gender": "female", "score1": 88, "score2": 89},
)
student3 = Student(
    "Hong",
    3,
    2,
    {"gender": "unknown", "score1": 78, "score2": 79},
)

# 확인
print(student1)
print(student2)
print(student3)
