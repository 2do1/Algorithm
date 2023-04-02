from collections import deque

def bfs(n):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k: # 동생을 찾았을 경우
            print(dist[x])
            return 
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and not dist[nx]: # 아직 방문하지 않고, 범위를 벗어나지 않았을 경우
                dist[nx] = dist[x] + 1
                queue.append(nx)

n, k = map(int, input().split())

answer = 0 # 가장 빠른 시간
dist = [0] * 100001
bfs(n)