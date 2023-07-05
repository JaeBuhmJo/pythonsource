# 반복문
# while, for

# 1~10 출력

i = 1
while i <11:
    print(i,end=' ')
    i += 1
print()
even = 0
while even <=100:
    if even%2==0:
        print(even, end=' ')
    even+=1
print()

num = 1
while num<10:
    print("3*%d = %d" % (num,3*num))
    num+=1

# in : 포함 : python에 y가 포함되어있니
print("in 기호")
print("y" in "python")



# range() : 범위 지정 함수
print(range(5))
print(list(range(2,5))) #2부터 포함, 5부터 불포함
print(list(range(2,50,3)))

# for
for i in range(10):
    print(i)

# for i in range(1,101):
#     print(i, end=" ")
# print()

# input = int(input())
# sum = 0
# for i in range(input+1):
#     sum+=i
# print(sum)

# sum() : 범위가 들어가면 총합 구해주는 함수
print(sum(range(1,11)))

for i in range(10, -1, -1):
    print(i, end=" ")

print()

for i in range(5):
    for j in range(5):
        print(i + j, end=" ")
    print()

# 구구단
for i in range(2,10):
    for j in range(1, 10):
        print("%d * %d = %d" % (i,j,i*j),end=" ")
    print()

#break, continue : 자바 개념과 동일
i = 1
while i <= 10:
    if i == 5:
        break
    print(i,end=" ")
    i += 1