# 파일 읽기

# f = open("resource/test1.txt","r",encoding="utf-8")
# print(f.read())
# f.close()

# readline() : 줄 단위로 읽어오기
# f = open("resource/test2.txt","r",encoding="utf-8")
# content = f.readline()
# print(content)
# f.close()
f = open("resource/test2.txt", "r", encoding="utf-8")
content = f.readline()
while content:
    print(content)
    content = f.readline()
f.close()

# readline() : 모든 줄 읽어오기
f = open("resource/test2.txt", "r", encoding="utf-8")
content = f.readlines()
print(content)
f.close()

f = open("resource/score.txt", "r", encoding="utf-8")
scores = [int(x) for x in f.readlines()]
summation = sum(scores)
print(summation)
print(summation / len(scores))

f = open("resource/info.txt", "r", encoding="utf-8")
# 이름 :
# 몸무게 :
# 키 :
# BMI : weight/(height/100)**2
# 결과 : 저체중?고체중?
# data = f.readline()
# while data:
#     name = data[:data.find(",")]
#     weight = int(data[data.find(",")+1:data.rfind(",")])
#     height = int(data[data.rfind(",")+1:])
#     print("이름 : %s" % name,end=" / ")
#     print("몸무게 : %d"%weight,end=" / ")
#     print("키 : %d"%height,end=" / ")
#     bmi = (weight/(height/100)**2)
#     print("BMI : %2.2f"% bmi,end=" / ")
#     if bmi >25:
#         result = "과체중"
#     elif bmi >18.5:
#         result = "정상체중"
#     else:
#         result = "저체중"
#     data = f.readline()
#     print("결과 : %s"% result)

# with open("resource/test1.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# 암호화된 파일을 읽어 원래대로 출력

print(ord("a"))
print(chr(97))

print(chr(ord("안") + 100))

while True:
    no = int(input("1. 암호화 | 2. 복호화 | 3. 종료 : "))
    if no == 1:
        with open("resource/origin.txt", "r", encoding="utf-8") as f:
            content = f.read()
        with open("resource/encry.txt", "w", encoding="utf-8") as f:
            for c in content:
                f.write(chr(ord(c) + 100))
    elif no == 2:
        with open("resource/encry.txt", "r", encoding="utf-8") as f:
            content = f.read()
            for c in content:
                print(chr(ord(c) - 100), end="")
    else:
        break

# rb, wb : text가 아닌 파일을 읽어올 때 -> read binary, write binary
