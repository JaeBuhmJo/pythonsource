# 변수 : 타입 없음, 값을 삽입 시 타입 결정
# 타입 : 숫자형 - int, float
#        문자형 - str
#        불 - bool
#        자료 구조 - list, set, dict, tuple


# 문자열 - "str", 'str', 
# 문자열 여러줄 - """str""", '''str'''

str1 = "Life is too short, You need Python."
str2 = 'Life is too short, You need Python.'
str3 = """Life is too short, You need Python."""
str4 = '''Life is too short, You need Python.'''

print(str1)
print(str2)
print(str3)
print(str4)

print()
num1 = num2 = 10
print(num1,num2)

num1, num2 = 10, 15
print(num1,num2)
num1, num2 = num2, num1 #
print(num1, num2)

num1 = "한글"
print(num1)

# 타입변환 문자열로 : str()
print(num1+str(num2))

# 연산자
a,b = 5,4
print("a + b = %d" % (a+b))
print("a - b = %d" % (a-b))
print("a * b = %d" % (a*b))
print("a / b = %f" % (a/b)) #진짜 나눗셈
print("a // b = %f" % (a//b)) # 몫 취하기
print("a %% b = %d" % (a%b))
print("a ** b = %d" % (a**b))

# type() : 변수 타입 확인
# str() : 문자열 변환, int(), float(), bool(), ..
x = str(3.5)
print(x,type(x))
print(int(True),type(int(True)))
print(int(False),type(int(False)))
print(bool(0.1),type(bool(0.1))) # 0 = false, 다른 숫자 모두 = True
print(float("98.99"),type(float("98")))
# print(int("98.99"),type(int("98.99"))) # float형태의 str은 int직접변환 불가

#동전 교환
money, c500, c100, c50, c10 = 0,0,0,0,0

money = 7777

print("500원 : %d개"% (money//500))
money %= 500
print("100원 : %d개"% (money//100))
money %= 100
print("50원 : %d개"% (money//50))
money %= 50
print("10원 : %d개"% (money//10))
money %= 10
print("나머지 : %d원"% money)


# ||, && (X) => or, and
a,b,c = 100,60,15
# print("and : ", a>b && a>c)
# print("and : ", a>b || a>c)
print("and : ", a>b and a>c)
print("and : ", a>b or a>c)

# ! (X) => not
# print(!True)
print(not True)