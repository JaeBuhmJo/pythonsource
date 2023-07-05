# class

# 학생 3명의 정보(이름, 학년, 반, 성별, 과목 점수) 저장

student_name_1 = "Kim"
student_grade_1 = 1
student_number_1 = 1
student_detail_1 = [
    {"gender": "male"},
    {"score1": 95},
    {"score2": 99},
]
student_name_2 = "Park"
student_grade_2 = 2
student_number_2 = 2
student_detail_2 = [
    {"gender": "female"},
    {"score1": 88},
    {"score2": 89},
]
student_name_3 = "Hong"
student_grade_3 = 1
student_number_3 = 3
student_detail_3 = [
    {"gender": "unknown"},
    {"score1": 78},
    {"score2": 79},
]

# 3명 학생 정보 출력
# 이름 : Kim, 학년 : 1, 번호 : 1, 학생정보 : detail

for i in range(1, 4):
    print(f"학생 {i} 정보:")
    print(f"- 이름: {globals()[f'student_name_{i}']}")
    print(f"- 학년: {globals()[f'student_grade_{i}']}")
    print(f"- 학번: {globals()[f'student_number_{i}']}")
    print(f"- 세부 정보: {globals()[f'student_detail_{i}']}")
    print()
