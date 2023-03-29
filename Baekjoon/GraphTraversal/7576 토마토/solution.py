from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()

        for index in range(4):
            nx = x + dx[index]
            ny = y + dy[index]
            # 맵 밖을 벗어나지 않았을 경우, 익지 않은 토마토일 경우
            if 0 <= nx < n and 0 <= ny < m and tomatos[nx][ny] == 0: 
                tomatos[nx][ny] = tomatos[x][y] + 1
                queue.append([nx, ny])
                

m, n = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1: # 토마토일 경우
            queue.append([i, j]) # 큐에 넣어준다.

bfs()

answer = 0 
for row in tomatos:
    if 0 in row: # 익지 않은 토마토가 있을 경우
        print(-1)
        exit(0)
    else:
        answer = max(answer, max(row))

print(answer - 1)