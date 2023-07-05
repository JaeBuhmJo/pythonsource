# 파이썬 자료형
# 4. 딕셔너리 (자바의 Map과 동일)
# {} 사용

# key 값은 str, int 가능
# value 값은 str, int, list, tuple, dict
dict1 = {"name":"park","age":12}
print(dict1)

# 특정 키에 해당하는 value 출력
print(dict1["name"])
print(dict1["age"])
# print(dict1["addr"])

dict2 = {0: "Hello Python", 1: "Hello Java"}
print(dict2)
print(dict2[0])

dict3 = {"arr" : [1,2,3,4]}
print(dict3)
print(dict3["arr"])

# 요소 추가
dict1["birth"] = "0616"
print(dict1)

dict2[2] = ["Hello Spring, Hello JSP"]
print(dict2)

dict3["rank"] = (16,17,18)
print(dict3)

# 각 숫자가 몇 개씩 나오는지 구한 후 딕셔너리 생성
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
dict4={}
for num in numbers:
    dict4[num]=numbers.count(num)
print(dict4)

# 요소 삭제
del dict1["birth"]
print(dict1)

# 함수
# get(키값)
# 있는 키 요청 : 사실상 동일
print(dict1.get("name"))
print(dict1["name"])

# 없는 키 요청
print(dict1.get("addr")) # None 리턴
# print(dict1["addr"]) # KeyError

# keys() : 딕셔너리 내 키 값 가져오기
print(dict1.keys())

# values()
print(dict1.values())

# entry
print(dict1.items())

# in : 키가 포함되어 있는가?
print("name" in dict1)
print(4 in dict2)

my_info = {"name":"kim","age":35,"city":"seoul"}

for k in my_info.keys():
    print(k)
for v in my_info.values():
    print(v)
for k,v in my_info.items():
    print(k,v)

info = {v for v in my_info.values()}
print(info)

info = [v for v in my_info.values()]
print(info)

score = {"A":90,"B":80,"C":70}

print(score.get("B"))
del score["B"]
print(score)

price = {"성인":10000,"청소년":7000,"아동":3000}

price["소아"]=0

print(price.keys())
print(price.values())

# list(), tuple()
print(list(price.keys()))
print(tuple(price.keys()))

print(type(score)) #<class 'dict'>
score.clear()
print(score)
