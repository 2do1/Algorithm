from collections import deque
r, c, t = list(map(int, input().split())) # t초가 지난 후

# 공기 청정기가 설치된곳은 -1
home = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 좌표
cleaner_x_y = [] 
for x in range(r):
    for y in range(c):
        if home[x][y] == -1:
            cleaner_x_y.append([x, y])
            

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t): # t초 동안

    dust = [[False] * c for _ in range(r)] # 미세먼지가 있는지 여부 표시
    temp = [[0] * c for _ in range(r)] # 미세먼지가 확산할때 미세먼지가 있는 칸은 나중에 더해주기 위해 저장할 리스트

    for x in range(r):
        for y in range(c):
            if home[x][y] >= 1:
                dust[x][y] = True


    # 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    for x in range(r):
        for y in range(c):
            if dust[x][y]: # 미세먼지일 경우
                
                count = 0 # 확산된 방향의 개수
                for index in range(4):
                    nx = x + dx[index]
                    ny = y + dy[index]
                    if 0 <= nx < r and 0 <= ny < c and home[nx][ny] != -1: # 공기청정기가 아니거나, 칸이 없는 경우가 아닐 경우
                        if dust[nx][ny]: # 동시에 확산하는 미세먼지가 있을 경우
                            temp[nx][ny] += int(home[x][y] / 5)
                        else: # 동시에 확산하는 미세먼지가 아닐 경우
                            home[nx][ny] += int(home[x][y] / 5)

                        count += 1
                
                home[x][y] = home[x][y] - int(home[x][y] / 5) * count # 남은 미세먼지의 양

    for x in range(r):
        for y in range(c):
            home[x][y] += temp[x][y]


    for index in range(len(cleaner_x_y)):
        if index == 0: # 반시계방향
            cleaner_x = cleaner_x_y[0][0]
            cleaner_y = cleaner_x_y[0][1] + 1
            prev = 0 # Swap 진행

            r_c_x = [0, -1, 0, 1]
            r_c_y = [1, 0, -1, 0]

            idx = 0
            while True:
                if cleaner_x == cleaner_x_y[0][0] and cleaner_y == 0: # 공기청정기 좌표로 왔을 경우
                    break

                nx = cleaner_x + r_c_x[idx]
                ny = cleaner_y + r_c_y[idx]

                if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위를 넘어갔을 경우
                    idx += 1
                    continue
                
                home[cleaner_x][cleaner_y], prev = prev, home[cleaner_x][cleaner_y] # Swap 진행

                cleaner_x = nx
                cleaner_y = ny
                    
        
        elif index == 1: # 시계방향
            cleaner_x = cleaner_x_y[1][0]
            cleaner_y = cleaner_x_y[1][1] + 1
            prev = 0 # Swap 진행

            c_x = [0, 1, 0, -1]
            c_y = [1, 0, -1, 0]

            idx = 0
            while True:
                if cleaner_x == cleaner_x_y[1][0] and cleaner_y == 0: # 공기청정기 좌표로 왔을 경우
                    break

                nx = cleaner_x + c_x[idx]
                ny = cleaner_y + c_y[idx]

                if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위를 넘어갔을 경우
                    idx += 1
                    continue
                
                home[cleaner_x][cleaner_y], prev = prev, home[cleaner_x][cleaner_y] # Swap 진행

                cleaner_x = nx
                cleaner_y = ny
    
answer = 0 # 남아있는 미세먼지 양
for row in home:
    answer += sum(row)

answer += 2 # 공기청정기 값만큼 더해준다.

print(answer)