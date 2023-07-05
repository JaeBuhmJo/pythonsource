# class UserInfo:
#     """
#     Author : Hong
#     Date : 2023.06.21
#     Description : 클래스 작성법
#     """

#     def user_info(self):
#         print("메소드 실행")


# # default 생성자 같은 개념으로 인해 그냥 생성됐음

# user1 = UserInfo()
# user1.user_info()
# print(user1)  # object 찍으면 주소가 나옴


# class UserInfo:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def user_info(self):
#         print("메소드 실행")

#     def user_info(self):
#         return f"name : {self.name}, age : {self.age}"


# # 두 명의 객체 생성

# # user_info 호출
# user1 = UserInfo("Hong", 33)
# user2 = UserInfo("Kim", 24)


# print(user1.user_info())
# print(user2.user_info())
# class UserInfo:
#     user_count = 0

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#         UserInfo.user_count += 1

#     def user_info(self):
#         return f"name : {self.name}, age : {self.age}"

#     def __del__(self):
#         UserInfo.user_count -= 1

#     @classmethod
#     def function1(cls):
#         """
#         self를 붙이지 않으면 클래스 메소드가 된다
#         """
#         print("function1 호출", cls.user_count)

#     def function2(self):
#         print("function2 호출")


# user1 = UserInfo("홍길동", 30)
# user2 = UserInfo("김유신", 20)

# print(user1.user_info())
# print(user2.user_info())

# print("생성된 user {} 명".format(UserInfo.user_count))
# print("생성된 user {} 명".format(user1.user_count))

# del user1
# print("생성된 user {} 명".format(UserInfo.user_count))

# # user2.function2() 이거는 에러남
# UserInfo.function1()  # 이거는 스태틱메소드
# user2.function2()


class UserInfo:
    """
    이메일은 들어올수도 아닐 수도 있는 파라미터
    """

    def __init__(self, name, age, email=None) -> None:
        self.name = name
        self.age = age
        self.email = email

    def user_info(self):
        print("메소드 실행")

    def user_info(self):
        return f"name : {self.name}, age : {self.age}, email : {self.email}"


user1 = UserInfo("홍길동", 30, "hong@naver.com")
user2 = UserInfo("김유신", 20)

print(user1.user_info())
print(user2.user_info())
