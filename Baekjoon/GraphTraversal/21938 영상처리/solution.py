from collections import deque

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        
        for index in range(4):
            nx = x + dx[index]
            ny = y + dy[index]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            
            if screens[nx][ny] == 255 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True

n, m = map(int, input().split()) # 세로 N, 가로 M
pixels = [list(map(int, input().split())) for _ in range(n)]
screens = [] 
visited = [[False] * m for _ in range(n)]
answer = 0 # 물체의 개수

t = int(input()) # 경계값 T

for pixel in pixels:
    screen = []
    for index in range(0, m * 3, 3):
        rgb_average = sum(pixel[index:index + 3]) // 3 # 세가지 색상 평균 
        if rgb_average >= t:
            screen.append(255)
            continue
        screen.append(0)
    
    screens.append(screen)

for i in range(n):
    for j in range(m):
        if screens[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            answer += 1

print(answer)