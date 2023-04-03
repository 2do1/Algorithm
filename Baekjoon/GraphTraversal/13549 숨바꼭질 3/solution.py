from collections import deque

# def bfs(x):
#     queue = deque()
#     queue.append(x)
#     visited[x] = True

#     while queue:
#         x = queue.popleft()
#         if x == k: # 동생을 찾았을 경우
#             print(dist[k])
#             return

#         for nx in (x * 2, x - 1, x + 1): # 순간이동 먼저
#             if 0 <= nx <= 100000 and not visited[nx]: # 아직 방문하지 않았고, 범위를 벗어나지 않았을 경우      
#                 if nx == x * 2: # 순간이동
#                     dist[nx] = dist[x]
#                 else: # 걷는 경우
#                     dist[nx] = dist[x] + 1

#                 visited[nx] = True
#                 queue.append(nx)

# appendleft() 사용
def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        x = queue.popleft()
        if x == k: # 동생을 찾았을 경우
            print(dist[k])
            return

        for nx in (x - 1, x + 1, x * 2): # 순간이동 먼저
            if 0 <= nx <= 100000 and not visited[nx]: # 아직 방문하지 않았고, 범위를 벗어나지 않았을 경우      
                if nx == x * 2: # 순간이동
                    dist[nx] = dist[x]
                    queue.appendleft(nx) # 순간이동 먼저 탐색
                else: # 걷는 경우
                    dist[nx] = dist[x] + 1
                    queue.append(nx)

                visited[nx] = True
                

n, k = map(int, input().split())

dist = [0] * 100001
visited = [False] * 100001

bfs(n)