from collections import deque

n, m = map(int, input().split()) # 세로 크기 n, 가로 크기 m

graph = [list(map(int, input().split())) for _ in range(n)] # 도화지
visited = [[False] * m for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append([x, y])
    visited[x][y] = True # 방문 처리
    area = 1 # 넓이

    while queue: # 큐가 빌 때 까지
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 도화지 밖으로 벗어났을 경우
                continue
            
            if graph[nx][ny] == 0: # 색칠이 안된 부분일 경우
                continue
    
            if graph[nx][ny] == 1 and not visited[nx][ny]: # 색칠이 된 부분일 경우, 방문하지 않은 곳일 경우
                visited[nx][ny] = True
                queue.append([nx, ny])
                area += 1

    return area

total = 0 # 그림의 개수
max_area = 0 # 가장 넓은 그림의 넓이

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]: # 색칠이 된 부분일 경우, 방문하지 않은 곳일 경우
            area = bfs(i, j) 
            total += 1
            max_area = max(max_area, area)

print(total)
print(max_area)