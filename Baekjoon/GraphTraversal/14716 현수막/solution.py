import sys
from collections import deque
sys.setrecursionlimit(100000)

m, n = map(int, input().split()) # 현수막 크기 m, n

graph = [list(map(int, input().split())) for _ in range(m)] # 현수막
visited = [[False] * n for _ in range(m)] # 방문 여부

answer = 0 # 글자의 개수 

# 위에서부터 시계방향으로, 대각선 포함
dx = [-1, -1, 0, 1, 1, 1, 0, - 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
    visited[x][y] = True # 방문 표시
    queue = deque()
    queue.append([x, y])

    while queue: # 큐가 빌때까지
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n: # 현수막 밖을 벗어났을 경우
                continue

            if not visited[nx][ny] and graph[nx][ny] == 1: # 방문하지 않았고, 글자인 부분일 경우
                visited[nx][ny] = True # 방문 표시
                queue.append([nx, ny])

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n: # 현수막 밖을 벗어났을 경우
        return False
    
    if not visited[x][y] and graph[x][y] == 1: # 방문하지 않았고, 글자인 부분일 경우
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y + 1)
        dfs(x + 1, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y - 1)
        dfs(x, y - 1)
        dfs(x - 1, y - 1)
        return True

    return False

# DFS 알고리즘
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1: # 방문하지 않았고, 글자인 부분일 경우
            if dfs(i, j):
                answer += 1
                
# BFS 알고리즘
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1: # 방문하지 않았고, 글자인 부분일 경우
            bfs(i, j)
            answer += 1

print(answer)