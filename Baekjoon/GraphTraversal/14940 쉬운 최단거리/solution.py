from collections import deque

n, m = map(int, input().split()) # 세로 n, 가로 m

graph = [list(map(int, input().split())) for _ in range(n)] # 세로 n
visited = [[False] * m for _ in range(n)] # 방문 여부
answer = [[-1] * m for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    answer[x][y] = 0

    while queue: # 큐가 빌때까지 계속
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: # 자도 밖으로 벗어났을 경우
                continue

            if graph[nx][ny] == 0: # 갈 수 없는 땅일 경우
                continue
            
            if graph[nx][ny] == 1 and not visited[nx][ny]: # 갈 수 있는 땅이고, 아직 방문하지 않았을 경우
                answer[nx][ny] = answer[x][y] + 1
                visited[nx][ny] = True
                queue.append([nx, ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: # 목표지점일 경우
            bfs(i, j)
        elif graph[i][j] == 0: # 벽일 경우
            answer[i][j] = 0

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()

for i in range(n):
    print(" ".join(map(str, answer[i])))

# find = False # 목표지점 찾았을 경우
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 2: # 목표지점일 경우
#             bfs(i, j)
#             find = True
#             break
#     if find:
#         break

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] != 0 and not visited[i][j]: # 방문하지 못한 곳이라면
#             print(-1, end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print() # 띄어쓰기

    
# 꼼수 풀이...
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0: # 갈 수 없는 땅일 경우
#             print(0, end=' ')
#         else:
#             print(graph[i][j] - 2, end=' ') # 한 줄 간격으로 출력
#     print() # 띄어쓰기 