from collections import deque

def bfs(start, end):
    if start == end:
        return 0
    
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        start = queue.popleft()

        for node in graph[start]:
            if not visited[node]:
                visited[node] = True
                check[node] = check[start] + 1
                if node == end:
                    return check[end]
                queue.append(node)

    return -1

a, b = map(int, input().split())

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
check = [0] * (n + 1)

for _ in range(m):
    node1, node2 = map(int ,input().split())

    graph[node1].append(node2)
    graph[node2].append(node1)

print(bfs(a, b))