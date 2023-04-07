n = int(input())


class_room = [[0] * (n) for _ in range(n)] 
students = [list(map(int, input().split())) for _ in range(n ** 2)]


# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students: 

    room_info = [] # 각 칸들의 인접한 정보를 담는 리스트, [좋아하는 학생의 수, 빈칸의 수]
    for x in range(n):
        for y in range(n):
            if class_room[x][y] == 0: # 빈칸일 경우
                like_count = 0 # 인접한 칸 좋아하는 학생 수
                blank_count = 0 # 인접한 칸 빈칸의 수
                for index in range(4):
                    nx = x + dx[index]
                    ny = y + dy[index]

                    if 0 <= nx < n and 0 <= ny < n: # 범위 체크
                        if class_room[nx][ny] in student[1:]: # 좋아하는 학생이 있을 경우
                            like_count += 1
                        elif class_room[nx][ny] == 0: # 빈칸일 경우
                            blank_count += 1

                # 좌표와 학생 수 빈칸 수를 담는다.
                room_info.append([x, y, like_count, blank_count])
    
    room_info = sorted(room_info, key=lambda x : (x[2], x[3]), reverse=True) # 인접한 칸이 많은 순, 그 다음 비어있느 칸 순으로 내림차순 정렬

    class_room[room_info[0][0]][room_info[0][1]] = student[0]


# 만족도 합 구하기
answer = 0 # 만족도 합

for x in range(n):
    for y in range(n):

        now_student = class_room[x][y] # 현재 칸에 있는 학생
        now_like_student = [] # 현재 칸에 있는 학생이 좋아하는 학생들

        for student in students:
            if student[0] == now_student: # 현재 칸에 있는 학생일 경우
                now_like_student = student[1:]
                break
                
        like_count = 0 # 인접한 칸에 좋아하는 학생이 몇명있는지
        for index in range(4):
            nx = x + dx[index]
            ny = y + dy[index]

            if 0 <= nx < n and 0 <= ny < n: # 범위 체크
                if class_room[nx][ny] in now_like_student: # 좋아하는 학생이 있을 경우
                    like_count += 1
        
        if like_count == 1:
            answer += 1
        elif like_count == 2:
            answer += 10
        elif like_count == 3:
            answer += 100
        elif like_count == 4:
            answer += 1000

print(answer)