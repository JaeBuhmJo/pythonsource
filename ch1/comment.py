# 주석

"""
여러 줄 주석 처리
"""

'''
여러 줄 주석 처리
'''

# 화면 출력 - print() / 변수타입 확인 - type()
print("Hello Python!!!")
print(25.3)
print(type(100)) #int
print(type("100")) #str
print(type('100')) #str
print(type(True)) #float
print(type(100.5)) #bool

    # print
# sep : 문자열 사이 구분자(기본값 : ' ')
print ('t','e','s','t')
print ('t','e','s','t',sep='-')

# end : 기본값은 개행문자. print의 마지막 추가문자 지정.
print("Welcome To", end=' ')
print("the black parade")

# format : %s(문자열, 정수, 실수 등 다 써도 됨), %d, %f, ...
print("%d"%100)
print("%5d"%100) # 5자리에 맞춰서 출력 - 오른쪽 정렬
print("%05d"%100) # 5자리에 맞춰서 출력 - 빈자리는 0으로 채움
print()
print("%s"%"hi")
print("%5s"%"hi")
print()
print("%-8.2f" % 123.21) # - : 왼쪽 정렬
print("%8.2f" % 123.21)
print("%8.2f" % 123.213456)

# 변수 선언(타입 선언 안함 - 값에 따라 타입 결정)
number=3
print("I eat %d apples" % number)
print("I eat", number, "apples")

print("%d : %s" % (1, "홍길동")) #포맷에 두 개 이상 들어가면 대입값 () 묶어주기

print("I eat %s apples" % 2)
print("I eat %s apples" % 3.156)
print("I eat %s apples" % "two")

# 98%
print("98%")
print("Error is %d%%"%98)

# format() 함수
print("\nformat 함수 : {}")
print("{} and {}".format("You","Me"))
print("I eat {0} apples".format("3"))
print("{1} and {0}".format("You","Me"))
print("{1} and {0} and {1}".format("You","Me"))
print("{var1} and {var2}".format(var1="You",var2="Me"))
print("{0} and {var2}".format("You",var2="Me"))
#print("{0} and {var2}".format(var1="You","Me")) 이거는 에러남

# 이스케이프 문자 : \n, \t
print("a\n줄바꿈\t탭 \\ \"")
print("\\n \\t \\\\ 그대로 출력")
print(r"\n \t \\ 그대로 출력")
print("글자가 '강조'되는 효과")
print('글자가 "강조"되는 효과')

