n = int(input()) # 정사각형의 한 변의 길이

graph = [list(map(int, input())) for _ in range(n)] # 지도

answer = [] # 단지내 집의 수들이 담긴 리스트

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n: # 지도 밖으로 벗어났을 경우
        return
    
    if graph[x][y] == 1: # 집이 있는 곳일 경우
        graph[x][y] = -1 # 방문 표시 해준다
        global total
        total += 1

        # 상하좌우로 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return total
    return

total = 0 # 단지 내 집의 수
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집이 있는 곳일 경우
            total = dfs(i, j)
            answer.append(total)
            total = 0
            
answer = sorted(answer) # 오름차순 정렬

print(len(answer)) # 총 단지수
for num in answer:
    print(num)