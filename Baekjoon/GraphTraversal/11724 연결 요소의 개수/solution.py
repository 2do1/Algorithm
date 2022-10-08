import sys
from collections import deque

sys.setrecursionlimit(5000)

n, m = map(int, sys.stdin.readline().split()) # 정점 개수 n, 간선 개수 m

connect_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)] # 연결 정보

graph = [[] for _ in range(n + 1)] # 그래프 

for connect in connect_list: # 그래프에 연결 정보 추가
    graph[connect[0]].append(connect[1])
    graph[connect[1]].append(connect[0])

visited = [False] * (n + 1) # 방문했는지의 여부

# BFS 알고리즘
def bfs(v, graph, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True # 방문 처리 해준다.

    while queue: # 큐가 빌때까지
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]: # 아직 방문하지 않은 곳이면
                queue.append(i)
                visited[i] = True # 방문 처리 해준다.
    
answer = 0
for i in range(1, n + 1):
    if not visited[i]: # 아직 방문하지 않은 곳이면
        bfs(i, graph, visited)
        answer += 1
print(answer)

# DFS 알고리즘
def dfs(v, graph, visited):
    visited[v] = True # 방문 표시

    for i in graph[v]:
        if not visited[i]: # 아직 방문하지 않은 곳이면
            dfs(i, graph, visited)    

answer = 0 # 연결 요소의 개수
for i in range(1, n + 1):
    if not visited[i]: # 아직 방문하지 않은 곳이면
        dfs(i, graph, visited)
        answer += 1

print(answer)