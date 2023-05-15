r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]
is_sunk = [[False] * c for _ in range(r)]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for x in range(r):
    for y in range(c):
        if graph[x][y] == 'X': # 섬일 경우
            sea_total = 0 # 인접한 칸에 바다 개수 
            for index in range(4):
                nx = x + dx[index]
                ny = y + dy[index]

                if 0 <= nx < r and 0 <= ny < c: # 지도 밖을 벗어나지 않았을 경우
                    if graph[nx][ny] == '.': # 바다일 경우
                        sea_total += 1
                else: # 지도 밖을 벗어났을 경우는 모두 바다이다.
                    sea_total += 1

            if sea_total >= 3: # 바다 개수 3개 또는 4개일 경우 땅은 잠김
                is_sunk[x][y] = True

for x in range(r):
    for y in range(c):
        if is_sunk[x][y]:
            graph[x][y] = '.'

# 상하 범위 정하기 
row_start, row_end = 0, 0 
for index, row in enumerate(graph):
    if 'X' in row:
        row_start = index
        break

for index in range(len(graph) - 1, -1, -1):
    if 'X' in graph[index]:
        row_end = index
        break


# 좌우 범위 정하기
col_index = []
for y in range(c):
    for x in range(row_start, row_end + 1):
        if graph[x][y] == 'X':
            col_index.append(y)
            break

col_start, col_end = col_index[0], col_index[-1] 
for row in graph[row_start:row_end + 1]:
    print(''.join(row[col_start:col_end + 1]))