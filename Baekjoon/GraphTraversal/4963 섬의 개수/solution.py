import sys
sys.setrecursionlimit(5000000) # 재귀 제한조건을 풀어준다.

# 가로, 세로, 대각선으로 연결되어 있을 경우 -> 걸어갈 수 있다.

def dfs(x, y): # 시작 좌표 (x, y), 지도 너비, 높이 (w, h)
    if x <= -1 or x >= h or y <= -1 or y >= w: # 지도 밖으로 벗어났을 경우
        return False
    
    if sea_map[x][y] == 1: # 땅일 경우에
        sea_map[x][y] = 0 # 방문한 땅이라는 것을 표시 
        dfs(x - 1, y) # 위
        dfs(x - 1, y + 1) # 오른쪽 위 대각선
        dfs(x, y + 1) # 오른쪽
        dfs(x + 1, y + 1) # 오른쪽 아래 대각선
        dfs(x + 1, y) # 아래
        dfs(x + 1, y - 1) # 왼쪽 아래 대각선
        dfs(x , y - 1) # 왼쪽
        dfs(x - 1, y - 1) # 왼쪽 위 대각선
        return True
    return False

while True:
    w, h = map(int, input().split()) # w: 지도의 너비, h: 지도의 높이

    if w == 0 and h == 0: # 마지막 입력일 경우
        break
    
    sea_map = [list(map(int, input().split())) for _ in range(h)] # 지도 입력받는다.

    island_count = 0 # 섬의 개수
    for i in range(h): # 섬의 개수 탐색 시작
        for j in range(w):
            if dfs(i, j) == True:
                island_count += 1
    
    print(island_count) # 섬의 개수 출력 

# # BFS 풀이
# from collections import deque

# def bfs(x, y):
#     dx = [1, -1, 0, 0, 1, -1, 1, -1]
#     dy = [0, 0, -1, 1, -1, 1, 1, -1]

#     sea_map[x][y] = 0 # 시작 지점 방문했다는 것 표시
#     queue = deque() # 큐 생성
#     queue.append([x, y]) # 시작 지점 큐에 삽입

#     while queue:
#         a, b = queue.popleft()
#         for i in range(8): # 상하좌우 대각선 총 8개
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if 0 <= nx < h and 0 <= ny < w and sea_map[nx][ny] == 1: # 지도 범위 안에 있고, 땅일 경우에
#                 sea_map[nx][ny] = 0 # 방문한 땅이라는 것을 표시 
#                 queue.append([nx, ny])

# while True:
#     w, h = map(int, input().split()) # w: 지도의 너비, h: 지도의 높이

#     if w == 0 and h == 0: # 마지막 입력일 경우
#         break
    
#     sea_map = [list(map(int, input().split())) for _ in range(h)] # 지도 입력받는다.
#     island_count = 0 # 섬의 개수
#     for i in range(h): # 섬의 개수 탐색 시작
#         for j in range(w):
#             if sea_map[i][j] == 1: # 땅일 경우
#                 bfs(i, j)
#                 island_count += 1
    
#     print(island_count) # 섬의 개수 출력 