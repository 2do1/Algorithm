from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)

    visited[x] = True

    while queue:
        x = queue.popleft() 

        for node in graph[x]:
            if not visited[node]:
                queue.append(node)
                check[node] = check[x] + 1
                visited[node] = True


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
check = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

bfs(1)
max_distance = max(check)

print(check.index(max_distance), end=" ") # 가장 작은 헛간 번호
print(max_distance, end=" ") # 헛간까지의 거리
print(check.count(max_distance)) # 헛간과 같은 거리를 갖는 헛간의 개수