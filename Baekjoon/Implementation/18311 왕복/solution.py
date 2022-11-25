n, k = map(int, input().split())

courses = list(map(int, input().split()))
courses_total = sum(courses)

if k > courses_total: # 시작위치로 돌아오는 과정일 경우
    k -= courses_total
    for index in range(len(courses) - 1, -1, - 1):
        k -= courses[index]
        if k < 0:
            answer = index + 1
            break
else:
    for index in range(len(courses)):
        k -= courses[index]
        if k < 0:
            answer = index + 1
            break
print(answer)


# 시간초과 
# n, k = map(int, input().split())
# courses_length = list(map(int, input().split()))

# courses = [0]
# for index in range(1, n + 1):
#     courses.append(sum(courses_length[:index]))

# answer = 0 # 지나고 있는 코스의 번호 
# if k > courses[-1]: # 시작위치로 돌아오는 과정일 경우
#     k -= courses[-1]
#     position = courses[-1] - k
#     for index in range(len(courses) - 1, 0, -1):
#         if courses[index] >= position and position >= courses[index - 1]:
#             answer = index
#             break
# else:  # 시작위치로 돌아오는 과정이 아닐 경우
#     for course in courses:
#         if k <= course:
#             answer = courses.index(course)
#             break

# print(answer)