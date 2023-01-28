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


n = int(input()) # 동기 수 
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
check = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split()) # 친구 관계

    graph[a].append(b)
    graph[b].append(a)

bfs(1)

answer = 0
for num in check:
    if num == 1 or num == 2: # 친구거나 친구의 친구일 때
        answer += 1
print(answer)