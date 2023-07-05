# 파이썬 자료형
# 1. 문자열
# "", '', """ """, ''' '''

# + : 결합
print("문자"+"열")

# * : 복제
print("Python"*3)

print("*"*50)

# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)
str1 = "Life is too short"
print(str1[3]) #마치 자바에서 char 배열 취급

# 슬라이싱
print("",str1[2:6])
print("",str1[:6])
print("",str1[:])
print("",str1[:-4]) #끝에서 제외될 인덱스

# len() : 길이 함수
print("str1 길이", len(str1))

str2 = "20230615Sunny"
# 년도, 날씨를 구별해서 변수에 담기

date = str2[:8]
weather = str2[8:]

print(date)
print(weather)

year = date[:4]
month = date[4:6]
day = date[6:]
print(year+" "+month+" "+day)
print(year, month, day, sep=".")

# 주민등록번호 001205-3234567
ssn = "001205-3234567"
if ssn[7:8] == "1" or ssn[7:8] == "3":
    print("남자")
else:
    print("여자")

str1 = "대한민국"
for s in str1:
    print(s)

#입력받은 숫자만큼 하트 출력
# hearts = input()

# for i in range(len(hearts)):
#     for j in range(int(hearts[i])):
#         print("♥",end="")
#     print()


# num3 = int(input())
# num2 = num3
# for i in range(num3):
#     for j in range(num2):
#         print("♥",end="")
#     num2-=1
#     print()

# 문자열 관련 함수
# count
print("/n문자열 관련 함수")
str1 = "hobby"
print("특정 문자",str1.count("b")) #포함된 개수

str1 = "python is best choice"

print(str1.find("b")) #indexOf. 없으면 -1 반환
print(str1.find("k")) 
print(str1.find("i",10)) 
print(str1.rfind("i")) 

# index() : 못 찾는 경우 에러 리턴
# print(str1.index("b")) 
# print(str1.index("k")) 

# startswith() / endswith()
print(str1.startswith("p"))
print(str1.endswith("p"))

# join() : 해당 문자열의 문자들 사이에 문자열 삽입.
str2 = ",.."
print(str2.join("abcde"))

# upper() / lower()
print("abcdef".upper())
print("abcdeF".lower())

# swapcase() : 대문자 -> 소문자 -> 대문자
str1 = "Python is Easy"
print(str1.swapcase())

# 공백 제거 : 왼쪽, 오른쪽, 양쪽
str1 = "    hi    "
print("1",str1,"1")
print("1",str1.lstrip(),"1")
print("1",str1.strip(),"1")
print("1",str1.rstrip(),"1")

# replace
str1 = "Life is too short"
print(str1.replace("Life", "Your Life"))

# split() => [] list 형태로 반환
print(str1.split())
a="abcd"
print(a.split())
a="a:b:c:d"
print(a.split(":"))
a="하나\n둘\n셋"
print(a.splitlines())
print(a.split())

# 문자열 구성 파악 - isdigit(), isalpha(), isalnum(), islower(), isupper() 등
print("12345".isdigit())
print("12345".isalpha())
print("12345".isalnum())

# 사이트별 비밀번호를 만들어 주는 프로그램
# https://www.naver.com
site = "https://www.naver.com"
# 규칙 1 : https:// 제외 ==> www.naver.com
site = site[site.find(".")+1:]
print(site)
# 규칙 2 : 처음 나오는 . 이후 부분은 제외
site = site[:site.find(".")]
print(site)
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 e 개수+ ! 구성
password = site[:3]
password += str(len(site))
password += str(site.count("e"))
password += "!"

print(password)
