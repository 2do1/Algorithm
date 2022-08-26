n = int(input()) # 학생의 수 n

student_list = sorted([input().split() for _ in range(n)], key=lambda x: x[1]) # 학생의 이름과 성적, 성적이 낮은 순서대로 

for student in student_list: # 성적이 낮은 순서대로 출력
    print(student[0], end=' ')