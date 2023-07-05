# 모듈 : 함수, 변수, 클래스를 모아놓은 파일

# 파이썬에서 제공하는 모듈 사용
import math

print(dir(math))
print(math.ceil(3.14))
print(math.sin(1))
print(math.cos(1))
print(math.floor(2.5))

import random

print(random.random())
# 10~20 사이의 임의의 float 리턴
print(random.uniform(10, 20))
# 지정값 사이의 임의의 int 리턴
print(random.randrange(1, 10))

print(random.choice([1, 2, 3, 4, 5, 6]))

list1 = list(range(10, 20))
print("생성된 리스트", list1)
random.shuffle(list1)
print("리스트 섞은 후", list1)

print(random.sample(list1, k=2))

import time

print("지금부터 5초 정지합니다.")
time.sleep(5)
print("프로그램 종료")
