import sys
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        start = queue.popleft()

        for node in graph[start]:
            if not visited[node]:
                check[node] = check[start] + 1
                visited[node] = True
                queue.append(node)

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
check = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

bfs(x)

if k not in check: # 최단 거리 k인 도시가 하나도 존재하지 않을 때
    print(-1)
else:
    for node in range(len(check)):
        if check[node] == k: # 최단거리가 k일 경우
            print(node) 