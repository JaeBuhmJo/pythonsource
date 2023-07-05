# 람다 함수
def square(x):
    return x * x
print(square(5))

square = lambda x: x*x
print(square(5))

add = lambda a, b: a + b
print(add(5,6))

def str_len(s):
    return len(s)

strings = ["bob","charles","alexander","teddy"]
strings.sort(key=str_len)
print(strings)

strings.sort(key=lambda s:len(s))
print(strings)

# filter(함수, 리스트)
even_list = []
def even(arr):
    for n in arr:
        if n%2 ==0:
            even_list.append(n)

list1 = [1,2,3,6,8,9,10,12]
even(list1)
print(even_list)

# list comprehension
even_list2 = [n for n in list1 if n%2==0]
print(even_list2)

# lambda + filter
def even2(n):
    return n%2==0

print(list(filter(even2,list1)))

print(list(filter(lambda n: n%2==0,list1)))

# lambda + map

def mul(x):
    return x**2

nums = [1,2,3,6,8,10,11,12,13,14,15]

# map(함수, 리스트)
print(list(map(mul, nums)))

print(list(map(lambda x: x**2, nums)))

nums = list(range(1,11))

def three(x):
    if x%3==0:
        return str(x)
    else:
        return x

print(list(map(three,nums)))
print(list(map(lambda x: str(x) if x%3==0 else x, nums)))
