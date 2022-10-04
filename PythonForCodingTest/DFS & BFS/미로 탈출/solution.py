from collections import deque

n, m = map(int, input().split()) 

maze = [list(map(int, input())) for _ in range(n)] # 미로

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque() # 큐 생성
    queue.append([x, y])

    while queue: # 큐가 빌때까지
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 미로 밖을 벗어날 경우
                continue

            if maze[nx][ny] == 0: # 괴물이 있을 경우 
                continue

            if maze[nx][ny] == 1: # 괴물이 없을 경우
                maze[nx][ny] = maze[x][y] + 1
                queue.append([nx, ny])
    return maze[n - 1][m - 1]

answer = bfs(0, 0)
print(answer)