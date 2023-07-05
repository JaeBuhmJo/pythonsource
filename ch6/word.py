import random
import time
import sqlite3
import datetime

word = []

# 시도횟수, 정답 개수
n, cor_cnt = 1, 0

# with 구문 word.txt 읽어서 words 리스트에 추가
# words 출력
# ['policy','number', ...]
# listWords = list()
# with open("resource/word.txt", "r", encoding="utf-8") as f:
#     for word in f:
#         words = word.replace("\n", "")
#         listWords.append(words)
# print(listWords)
words = list()
with open("resource/word.txt") as f:
    for w in f:
        words.append(w.strip())
print(words)

input("Ready? Press Enter Key")
start = time.time()
count = 0
while n <= 5:
    # 리스트 요소 임의로 섞기
    random.shuffle(words)
    question = random.choice(words)
    print("Question " + str(n))
    print(question)
    answer = input(": ")
    if answer == question:
        print("Correct!!")
        count += 1
    else:
        print("Wrong!!")
    n += 1
end = time.time()
print(f"{int(end - start)}초 동안 5문제 중 총 {count}문제 맞추셨습니다.")

# db에 저장
# 테이블 records 생성 : 정답개수(cor_cnt), 기록(record), 날짜(regdate, 현재 날짜와 시간)

# insert 작업
conn = sqlite3.connect("/source/pythonsource/resource/test.db", isolation_level=None)

cursor = conn.cursor()

result = "합격" if count >= 3 else "불합격"

# cursor.execute("create table questions (cor_cnt text, record text, regdate text)")
cursor.execute(
    "insert into questions(cor_cnt, record, regdate) values({},{},{})".format(
        count, result, datetime.datetime.now()
    )
)
