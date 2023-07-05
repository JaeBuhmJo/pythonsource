
# 
# 1~3번 메뉴만 선택 가능. 주차면수는 5면

# 2번을 선택 시 뒤에서부터 요소 제거.
# * 자동차 나감. 주차장 상태 => ['A','B','C']

parkingLot = []
top, car_name = 0, "A"

# print(ord("A"))
# print(chr(65))

while True : 
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))
    if no <= 3:
        if no == 1:
            pass
        elif no == 2:
            pass
        else:
            print("프로그램 종료")
            break

#메뉴 제공
# print("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 :", end=" ")
# parkingLot = []
# road = ["A","B","C","D","E"]
# top, car_name = 0, "A"
# open = True
# while open:
#     command = input()
#     if (command=="1"):
#         car_name = road.pop(0)
#         parkingLot.append(car_name)
#         print("%s 자동차 주차. 주차장 상태 => " % car_name, end=" ")
#         print(parkingLot)
#         print("도로 상황", end=" ")
#         print(road)
#     elif (command=="2"):
#         car_name = parkingLot.pop()
#         road.append(car_name)
#         print("%s 자동차 나감. 주차장 상태 => " % car_name,end=" ")
#         print(parkingLot)
#         print("도로 상황", end=" ")
#         print(road)
#     else:
#         open = False
#         print("주차장 프로그램 종료")
