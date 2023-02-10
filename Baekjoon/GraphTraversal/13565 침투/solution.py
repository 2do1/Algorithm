import sys
from collections import deque
sys.setrecursionlimit(1000000)

m, n = map(int, input().split())

graph = [list(map(int, input())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

# DFS 풀이
def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return 
    
    if not visited[x][y] and graph[x][y] == 0: # 전류가 잘통하는 흰색일 경우
        visited[x][y] = True
        # 상하좌우
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        
    return 

for index in range(n):
    if not visited[0][index] and graph[0][index] == 0:
        dfs(0, index)

if True in visited[-1]:
    print("YES")
else:
    print("NO")

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 풀이
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append([nx, ny])

for index in range(n):
    if not visited[0][index] and graph[0][index] == 0:
        bfs(0, index)

if True in visited[-1]:
    print("YES")
else:
    print("NO")