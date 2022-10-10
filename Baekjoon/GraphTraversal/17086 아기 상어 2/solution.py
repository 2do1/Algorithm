from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)] # 공간 가로 크기 m, 세로 크기 n

# 12시부터 시계방향 순서로 8방향 (대각선 포함)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

queue = deque()

def bfs():
    while queue: # 큐가 빌때까지
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 공간을 벗어 났을 경우
                continue
            
            if graph[nx][ny] == 0: # 빈 칸일 경우, 아직 방문하지 않았을 경우
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 상어가 있는 칸일 경우
            queue.append([i, j]) # 큐에 삽입해준다.

bfs() # 탐색 수행

answer = 0 # 안전 거리의 최댓값 
for i in range(n):
    for j in range(m):
        answer = max(answer, graph[i][j])

print(answer - 1)