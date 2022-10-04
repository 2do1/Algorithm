n, m = map(int, input().split()) # 세로 길이 n, 가로 길이 m

graph = [list(map(int, input())) for _ in range(n)] # 얼음 틀

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m: # 얼음 틀 밖으로 벗어났을 경우
        return False
    
    if graph[x][y] == 0: # 방문하지 않은 곳일 경우
        graph[x][y] = 1 # 방문처리 해준다.
        
        # 상하좌우로 탐색한다.
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1) 
        return True
    
    return False

answer = 0 # 아이스크림의 개수
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True: 
            answer += 1

print(answer)