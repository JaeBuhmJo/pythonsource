# 파일 입출력

# 파일 출력
# f = open("파일경로","모드")
# 파일 관련 작업
# ......

# 종료
# f.close()

# resource 폴더에 test1.txt 파일 생성
# "w" : 쓰기 모드
# 가상환경에서 작업할 때는 파이썬 소스 폴더에 있다고 생각하면 됨
# encoding="utf-8"

with open("resource/test1.txt", "w") as f:
    f.write("Hello Python")

# f = open("resource/test1.txt","w") 
# f.write("Hello Python")
# f.close()

# f = open("resource/test1.txt","w", encoding="utf-8")
# f.write("안녕하세요\n반갑습니다")
# f.close()

# 1~10 파일에 작성
# f = open("resource/test1.txt","w", encoding="utf-8")
# for i in range(1,11):
#     data = "%d\n" % i
#     f.write(data)
# f.close()

# 안녕하세요
# "a" : append 모드
# f = open("resource/test1.txt","a", encoding="utf-8")
# for i in range(1,11):
#     data = "안녕하세요\n"
#     f.write(data)
# f.close()

# list1 = ["홍길동\n","김길동\n","최길동\n"]
# f = open("resource/test2.txt","a", encoding="utf-8")
# f.writelines(list1)
# f.close()

dict1 = {"name":"홍길동","age":25,"addr":"서울"}
# test3.txt
# name : 홍길동
# age : 25
# addr : 서울

f = open("resource/test3.txt","w",encoding="utf-8")
for k in dict1.keys():
    f.write(k+" : "+str(dict1[k])+"\n")
f.close()

import random
hanguls= list("가나다라마바사아자차카타파하")
# print(hanguls)
# print(random.choice(hanguls))

f=open("resource/info.txt","w",encoding="utf-8")
for i in range(1000):
    name = random.choice(hanguls)+random.choice(hanguls)
    weight = random.randrange(40,100)
    height = random.randrange(140,190)
    f.write("{},{},{}\n".format(name, weight, height))
f.close()