import copy
n, m = map(int, input().split())

# 1번 행 n번 행 연결, 1번 열 n번 열 연결
a = [list(map(int, input().split())) for _ in range(n)]
# 구름이 있는지 여부를 확인
cloud = [[False] * n for _ in range(n)] 

# 처음 비바라기는 (N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)에 생성된다.
cloud[n - 1][0] = True
cloud[n - 1][1] = True
cloud[n - 2][0] = True
cloud[n - 2][1] = True


# 편의를 위해 1번째 인덱스부터 방향 값 저장
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]    

# 왼쪽 위 대각선부터
dia_x = [-1, -1, 1, 1]
dia_y = [-1, 1, 1, -1]

for _ in range(m):
    di, si = map(int, input().split())

    cloud_tmp = [[False] * n for _ in range(n)] # 임시의 값
    for x in range(n):
        for y in range(n):
            if cloud[x][y]: # 구름이 있을 경우
                nx = x
                ny = y
                for _ in range(si): # si칸 이동
                    nx += dx[di] 
                    ny += dy[di]

                    if nx < 0:
                        nx = n - 1
                    elif nx >= n:
                        nx = 0

                    if ny < 0:
                       ny = n - 1
                    elif ny >= n:
                        ny = 0 
                cloud_tmp[nx][ny] = True
                a[nx][ny] += 1 # 구름있는 칸 비 1씩 내린다.
    
    cloud = copy.deepcopy(cloud_tmp)

    disappear_x_y = [] # 구름이 사라진 좌표들
    for x in range(n):
        for y in range(n):
            if cloud[x][y]: # 구름이 있을 경우
                count = 0 # 4개의 방향 중 물이 있는 개수
                for index in range(4):
                    nx = x + dia_x[index]
                    ny = y + dia_y[index]

                    if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > 0: # 물이 있을 경우
                        count += 1
                
                a[x][y] += count # 4 방향에 물이 있는 개수만큼 더해준다.
                disappear_x_y.append([x, y])

    # 구름이 생성되는데 이전에 구름이 사라진 칸이 아니어야 한다.
    for x in range(n):
        for y in range(n):
            if not cloud[x][y] and a[x][y] >= 2: # 이전에 구름이 사라진 칸이 아니고, 물의 양이 2 이상일 경우
                a[x][y] -= 2 # 물의 양이 2만큼 줄어듬
                cloud[x][y] = True # 구름이 생성됨

    for x, y in disappear_x_y:
        cloud[x][y] = False                            

answer = 0 # 바구니에 들어 있는 물의 양의 합
for row in a:
    answer += sum(row)

print(answer)