# 함수
# 함수?(자바스크립트, 파이썬) 메소드? ==> 기능 정의
# 함수 : 단독으로 실행
# 메소드 : 클래스 내부에 선언, 객체 생성 후 실행

# 함수 정의
def hello():
    print("Hello")

def add(a,b):
    return a+b

print(add(3,4))

# 기본값 : n=2 => 함수 호출 시 값이 넘어오지 않는다면 기본값을 2로 지정

def print_n_times(value, n=2):
    for i in range(n):
        print(i, value)

print_n_times("안녕하세요",3)
print_n_times("반갑습니다")

# 가변 파라메터 : 파라메터의 개수가 일정치 않음
def add_many(*args):
    print(args)

add_many({"dessert":"macaroon","wine":"merlot"})
add_many("35","24","48")
add_many(["A","B","C","D"])
# 출력 결과가 tuple 형태로 나옴

def add_many2(*args):
    print(sum(args))

add_many2(1,2,3)
add_many2(1,2,3,4,5,6)

# 가변 파라메터는 여러개 받을 수 있어서, 맨 뒤로 보내야 나머지 변수가 인식이 된다.
def sum_mul(choice, *args):
    if choice == "mul":
        result = 1
        for i in args:
            result*=i
    elif choice == "add":
        result = 0
        for i in args:
            result+=i
    print(result)

sum_mul("mul",1,2,3,4,5,6)
sum_mul("add",1,2,3,4,5,6)

# **kwargs : 키워드 파라미터(key=value)
def args_func1(**kwargs):
    print(kwargs)

args_func1(name="park")
args_func1(name="park", age=12)
args_func1(name="park", age=12, title="python")

# 일반, 기본 파라메터, 가변 파라메터, 키워드 파라메터
def example_mul(arg1, arg2=15, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20)
example_mul(10)
example_mul(10, 20, "park", "kim")
example_mul(10, 20, "park", "kim", age=25, name="cho")

# 다중 리턴
def sum_and_mul(a, b):
    return a+b, a*b

print(sum_and_mul(5,6))

add1, sum1 = sum_and_mul(5,6)
print(add1)
print(sum1)

def func_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300

    return y1, y2, y3

r1, r2, r3 = func_mul(100)
print(r1,r2,r3)

def func_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300

    return [y1, y2, y3]

r1, r2, r3 = func_mul(100)
print(r1,r2,r3)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다"%nick)

say_nick("바보")
say_nick("야호")

# 두 개의 인자와 연산자를 받아 사칙연산을 수행하는 함수 작성

# def calc(num1, num2, op):
#     if op =="+":
#         result = num1+num2
#     if op =="-":
#         result = num1-num2
#     if op =="*":
#         result = num1*num2
#     if op =="/":
#         result = num1/num2
#     return result

# num1 = int(input("숫자 1 입력 : "))
# op = input("연산자 입력 : ")
# num2 = int(input("숫자 2 입력 : "))
# print("{}{}{}={}".format(num1,op,num2,calc(num1,num2,op)))

import random
print(random.randrange(1,46))

lotto = set()
while len(lotto)<6 :
    ball = random.randrange(1,46)
    if(ball not in lotto):
        lotto.add(ball)
listLotto = list(lotto)
listLotto.sort()
print(listLotto)

a=1
#a를 함수 내부에서 선언하지 않았기 때문에, unboundLocalError
def func1():
    global a
    a += 3
    print(a)

func1()

