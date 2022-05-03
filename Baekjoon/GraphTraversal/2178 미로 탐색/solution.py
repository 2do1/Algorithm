from collections import deque
n, m = map(int, input().split())

# 상, 하, 좌, 우 순서
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

maze = [] # 미로
for i in range(n):
    maze.append(list(map(int, input()))) # 미로 만들어주기

def bfs(x, y):
    queue = deque() # 큐 생성
    queue.append((x, y)) # 큐에 삽입 

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 미로 밖으로 나갔을 경우 
                continue
            
            if maze[nx][ny] == 1: # 이동할 수 있는 칸일 경우 
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
            else: # 이동할 수 없는 칸이거나, 이미 지나온 칸일 경우
                continue

    return maze[n-1][m-1]

answer = bfs(0, 0)
print(answer)
