from collections import deque

# BFS 풀이
def bfs(num1):
    queue = deque()
    queue.append(num1)
    visited[num1] = True

    while queue:
        x = queue.popleft()

        for node in graph[x]:
            if not visited[node]:
                check[node] = check[x] + 1
                queue.append(node)
                visited[node] = True

# DFS 풀이
def dfs(num1):
    visited[num1] = True
    for node in graph[num1]:
        if not visited[node]:
            check[node] = check[num1] + 1
            dfs(node)

n = int(input()) 

num1, num2 = map(int, input().split())

check = [0] * (n + 1)
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
# BFS 풀이
# bfs(num1) 

# DFS 풀이
dfs(num1)

if check[num2]:
    print(check[num2])
else:
    print(-1)