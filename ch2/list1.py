# 파이썬 자료형
# 2. 리스트
# []

# 리스트 생성

list1 = []
list2 = ['a',1,3.15,True]
print(list1)
print(list2)
list3 = ["a",1 , 3.15, True, ["b",  35, 45]]
print(list3)
# list4 = list(1,2,3)
# print(list4)

# 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1]) #끝에서 첫번째

print(list3[-1])
print(list3[-1][1])

# 리스트 슬라이싱
print(list2[0:2])
print(list3[:-1])
print(list3[4:])

list4 = [1, 2, ["a", "b", ["Life", "is"]]]
print(list4[2][2][1])

a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a[0]+b[1])

print(a*3)

# 리스트 특정 요소 수정
a[1] = 7
print(a)

a[2] = "Life"
print(a)

b[1:2] = [10,11] # 칸이 늘어나네?
print(b)

b[1] = [15,16,17]
print(b)

# 리스트 요소 삭제
del b[1]
print(b)

numbers = [273, 103, 5, 32, 65, 9, 72]
for number in numbers:
    if number >= 100:
        print("100 이상의 수 ", number)

for number in numbers:
    print("%d의 자릿수는 %d 입니다." % (number, len(str(number))))

# () : 튜플
list4 = list([1,2,3])
print(list4)

# 리스트 함수
# append() : 리스트 뒤에 요소 추가
list4.append(5)
print(list4)
list4.append([6,7,8])
print(list4)

# sort() : 원본 변경
alpha = ["a","z","A","b","D","f"]
alpha.sort()
print(alpha)

han = ["고양이","강아지","원숭이","호랑이"]
han.sort()
print(han)
han.sort(reverse=True)
print(han)
han.reverse()
print(han)

# insert(위치,요소)
han.insert(1, "악어")
print(han)

# remove(삭제할 요소)
# list = [1,3,3,5] ==> list.remove(3) : 첫번째 찾은 3만 제거
han.insert(1,"고양이")
print(han)
han.remove("고양이")
print(han)
print(han.pop())
print(han)

print(han.pop(2))
print(han)

# count()
han.insert(1,"원숭이")
print(han)
print(han.count("원숭이"))

# clear() : 리스트 안의 모든 요소 삭제
han.clear()
print(han)

if han:
    print("True")
else:
    print("False")
#비어있는 리스트 => False 처리

str = ""
if str:
    print("True")
else:
    print("False")
#비어있는 문자열 => False

# in
print("p" in "python")
print("p" in "java")

fruits = ["사과","딸기","배","자몽"]
print("사과" in fruits)
print("메론" not in fruits)

for fruit in fruits:
    print(fruit, end="+")
print()

# enumerate() : 튜플 구조로, index 포함된 채 iter
for fruit in enumerate(fruits):
    print(fruit)

for idx, fruti in enumerate(fruits):
    print(idx, fruti)

for idx, fruti in enumerate(fruits, start=2):
    print(idx, fruti)

score = [70,60,55,75,95,90,80,85,100,88]
summation = 0
for i in score:
    summation+=i
print(summation/10)

print((sum(score)/len(score)))

# 1~20 리스트 생성
list1 = [3]
list1 = list(range(1,21))
print(list1)

list3 = []
for x in range(1,101):
    list3.append(x)
print(list3)

# comprehension
list3 = [x for x in range(1,101)]
print(list3)

list4 = ["갑","을","병","정","경"]

list5 = [x for x in list4 if x != "정"]
print(list5)

#1 ~ 100 숫자 중 홀수
list6 = [x for x in range(1,101) if x%2!=0]
print(list6)

list9 = ["A", "b", "c", "D", "e", "F", "G", "h"]
listLower = [x for x in list9 if x.islower()]
print(listLower)

print([x*x for x in [0,1,2,3,4,5]])

list10 = [1,2,3]
list11 = []
add = 0
for x in range(3):
    list11.append([])
    for y in list10:
        list11[x].append(y+add)
    add+=1
print(list11)

list1 = [1,2,3]
list2 = []
for x in list1:
    list2.append([x,x+1,x+2])
print(list2)

print([[x,x+1,x+2] for x in list1])
