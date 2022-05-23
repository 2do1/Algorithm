students = [i for i in range(1, 31)] # 30명의 학생이 담긴 리스트

for _ in range(28): # 과제 제출한 학생 28명들을 리스트에서 제거한다.
    students.remove(int(input())) 

students.sort() # 오름차순 정렬 후

for student in students: # 과제 제출 안한 학생들을 출력한다.
    print(student) 

# 정렬할 필요가 없다.
# print(min(students))
# print(max(students))

# 2명만 출력해는건데 굳이 for문을 써야 했을까..
# print(students[0])
# print(students[1])