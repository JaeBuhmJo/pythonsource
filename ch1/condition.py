# 조건문

# if, if~else, if~elif
# {} 사용 안함, 스페이스바 4개 사용.

if True:
    print("True")

a=200
if a<100:
    print("a는 100보다 작다")
print("조건문에서 하나의 블럭 개념은 들여쓰기로 구분")

if a>100 and a<=200:
    print("a는 100보다 크고 200보다 작거나 같다.")
if 100 < a <=200:
    print("a는 100보다 크고 200보다 작거나 같다.")

#세 개의 변수 선언, 12, 6, 18 값 담기
#if 만으로 가장 큰 수 찾기

a, b, c = 12, 6, 18

if a>b and a> c:
    print(a)

a = 55
if a< 100:
    print("a는 100 보다 작다")
else:
    print("a는 100보다 크다")

# num = int(input())
# if num%2==0:
#     print("짝")
# else:
#     print("홀")

import datetime
now = datetime.datetime.now()
print(now)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

#오전 오후 출력

if now.hour<12 :
    print("오전")
else:
    print("오후")

# 삼항연산자 now.hour < 12 ? "오전" : "오후" (X)
# 참일 때 실행 구문 if 조건 else 거짓일 때 실행구문
str = "안녕하세요" if True else "반갑습니다"
print(str)
a=4
str = "안녕하세요" if a>5 else "반갑습니다"
print(str)

print("오전" if now.hour<12 else "오후")

# 다중조건 if ~ elif ~ else
num = 90
if num >= 90:
    print("A 등급")
elif num >= 80:
    print("B 등급")
elif num >= 70:
    print("C 등급")
elif num >= 60:
    print("D 등급")
else:
    print("F 등급")

# age, height 변수 선언, 27, 180 입력
# 나이가 20세 이상 지원 가능

age, height = 20, 159

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

# 계산기 : 두 개의 수 입력, 연산자(+-*/ // % **) 입력
num1 = int(input())
oper = input()
num2 = int(input())

if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='*':
    print(num1*num2)
elif oper=='/':
    print(num1/num2)
elif oper=='//':
    print(num1//num2)
elif oper=='%':
    print(num1%num2)
elif oper=='**':
    print(num1**num2)
    
    
