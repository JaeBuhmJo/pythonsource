# csv 읽기
import csv  # python에서 csv 를 다루는 모듈

# with open("resource/sample1.csv", "r") as f:
#     content = csv.reader(f)
#     print(content)
#     print(dir(content))
#     print(type(content))

#     next(content)  # 맨 위부터 한 행씩 제거

#     for c in content: # 행을 순차적으로, 리스트 형태로 가져온다.
#         print(c)
# csv 읽기

# with open("resource/sample2.csv", "r") as f:
#     content = csv.DictReader(f, delimiter="|")  # DictReader : 딕셔너리 형태로 가져옴

#     for c in content:
#         for k, v in c.items():
#             print(k, ":", v)
#         print()

# with open("resource/sample3.csv", "r") as f:
#     content = csv.reader(f)

#     for row in content:
#         # print(c)
#         for i in row:
#             print(i, end=" ")
#         print()

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open("resource/sample5.csv", "w", newline="") as f:
    wt = csv.writer(f)

    # for v in data:
    #     wt.writerow(v)
    wt.writerows(data)
