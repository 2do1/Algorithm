import sys
sys.setrecursionlimit(50000)
# from collections import deque

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS 풀이
# def bfs(x, y):
#     queue = deque()
#     queue.append([x, y])
#     visited[x][y] = True

#     wolves = 0
#     sheeps = 0
    
#     if yard[x][y] == 'v': # 늑대일 경우
#         wolves += 1
#     elif yard[x][y] == 'k': # 양일 경우
#         sheeps += 1

#     while queue:
#         x, y = queue.popleft()

#         for index in range(4):
#             nx = x + dx[index]
#             ny = y + dy[index]

#             # 맵 밖을 벗어났지 않을 경우
#             # 이전에 방문하지 않았을 경우
#             # 울타리가 아닐 경우
#             if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and yard[nx][ny] != '#':
#                 if yard[nx][ny] == 'v': # 늑대일 경우
#                     wolves += 1
#                 elif yard[nx][ny] == 'k': # 양일 경우
#                     sheeps += 1
#                 queue.append([nx, ny])
#                 visited[nx][ny] = True
                
#     return sheeps, wolves

# DFS 풀이
def dfs(x, y):
    global sheeps, wolves, visited

    if not visited[x][y] and yard[x][y] == 'v':
        wolves += 1
    elif not visited[x][y] and yard[x][y] == 'k':
        sheeps += 1
    
    if 0 <= x < r and 0 <= y < c and not visited[x][y] and yard[x][y] != '#':
        visited[x][y] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)



r, c = map(int, input().split())

yard = [list(input()) for _ in range(r)] 
visited = [[False] * c for _ in range(r)] # 방문 여부 

sheeps_count = 0
wolves_count = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and (yard[i][j] == "v" or yard[i][j] == "k"):
            # sheeps, wolves = bfs(i, j) BFS 알고리즘
            sheeps = 0
            wolves = 0

            dfs(i, j)
            if sheeps > wolves: # 양이 늑대보다 더 많을 경우
                sheeps_count += sheeps
            else: # 늑대가 양 이상일 경우
                wolves_count += wolves

print(str(sheeps_count) + " " + str(wolves_count))