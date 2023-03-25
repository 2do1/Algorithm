n = int(input()) # 도시의 수

road_costs = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = 2e9

def dfs(start, cost, depth):
    global answer

    if depth == n and road_costs[start][0] != 0:
        answer = min(answer, cost + road_costs[start][0])
        return

    for i in range(n):
        if not visited[i] and road_costs[start][i] != 0:
            visited[i] = True
            dfs(i, cost + road_costs[start][i], depth + 1)
            visited[i] = False
            

visited[0] = True
dfs(0, 0, 1)
print(answer)