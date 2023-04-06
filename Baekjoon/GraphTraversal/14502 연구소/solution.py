import copy

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m and not visited[x][y] and lab_copy[x][y] != 1: # 벽이 아니고 범위 안에 있을 경우, 방문하지 않았을 경우
        visited[x][y] = True
        lab_copy[x][y] = 2
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    return 

n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]
lab_copy = lab.copy()

# 새로 세울 수 있는 벽의 개수는 3개이고, 꼭 세워야 한다.
# 0은 빈 칸, 1은 벽, 2는 바이러스 
# 완전 탐색을 진행해야 한다.

blank_x_y = [] # 빈 칸의 좌표들
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0: # 빈 칸일 경우
            blank_x_y.append([i, j])

answer = -2e9 # 안전 영역의 최대 크기
for i in range(len(blank_x_y)):
    for j in range(i + 1, len(blank_x_y)):
        for k in range(j + 1, len(blank_x_y)):
            
            lab_copy = copy.deepcopy(lab) # 이중 리스트를 복사하려면 copy 모듈의 deepcopy()를 사용해야 한다
            # 벽 설정
            lab_copy[blank_x_y[i][0]][blank_x_y[i][1]] = 1
            lab_copy[blank_x_y[j][0]][blank_x_y[j][1]] = 1
            lab_copy[blank_x_y[k][0]][blank_x_y[k][1]] = 1

            visited = [[False] * m for _ in range(n)] # 방문 표시 여부

            for x in range(n):
                for y in range(m):
                    if not visited[x][y] and lab_copy[x][y] == 2: # 바이러스 일 경우
                        dfs(x, y)
        
            total = 0 # 안전 영역의 크기
            for row in lab_copy:
                total += row.count(0)
            
            answer = max(answer, total)

print(answer)