from collections import deque

n, l, r = map(int, input().split()) # n x n 크기의 땅, l명, r명

graph = [list(map(int, input().split())) for _ in range(n)] # 땅

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    union = [[x, y]] # 한 연합

    while queue: # 큐가 빌 때까지
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if not visited[nx][ny] and l <= abs(graph[nx][ny] - graph[x][y]) <= r: # 인구 차이가 l명 이상, r명 이하일 경우, 아직 방문하지 않은 곳일 경우
                queue.append([nx, ny])
                visited[nx][ny] = True
                union.append([nx, ny]) # 연합
    return union


answer = 0 # 인구 이동이 며칠 동안 발생하는지
while True:
    visited = [[False] * n for _ in range(n)]
    unions = [] # 연합들

    for i in range(n):
        for j in range(n):
            if not visited[i][j]: # 아직 방문하지 않은 경우
                union = bfs(i, j) # 연합을 이루고 있는 각 칸의 좌표들
                if len(union) > 1: # 연합을 이루고 있는 칸의 개수가 2이상일 때, 자기 자신을 제외하고 다른 칸을 포함할 때
                    unions.append(union)

    if len(unions) == 0: # 연합이 존재하지 않을 경우
        break
    
    for union in unions:
        total = 0
        for [x, y] in union: # 칸의 좌표
            total += graph[x][y]
        total //= len(union)
        for [x, y] in union:
            graph[x][y] = total # 인구 이동 진행
    answer += 1

print(answer)