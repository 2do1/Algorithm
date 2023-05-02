import sys
from collections import deque

sys.setrecursionlimit(1000000)

# BFS 알고리즘 
def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        x = queue.popleft()

        for node in tree[x]:
            if not visited[node]:
                visited[x] = True
                queue.append(node)
                parent_nodes[node] = x # 부모 노드를 기록해준다.

# DFS 알고리즘
def dfs(x):
    for node in tree[x]:
        if not visited[node]:
            visited[node] = True
            parent_nodes[node] = x # 부모 노드를 기록해준다.
            dfs(node)

n = int(input()) # 노드의 개수

tree = [[] for _ in range(n + 1)]

# 트리 자료구조
for _ in range(n - 1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n + 1)
parent_nodes = [0] * (n + 1) # 부모 노드 기록
# bfs(1) # BFS 알고리즘
dfs(1) # DFS 알고리즘

for index in range(2, n + 1):
    print(parent_nodes[index])