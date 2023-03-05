from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    wolf_count = 0
    sheep_count = 0

    if yard[x][y] == "v": # 늑대일 경우
        wolf_count += 1
    elif yard[x][y] == "o": # 양일 경우
        sheep_count += 1

    while queue:
        x, y = queue.popleft()

        for index in range(4):
            nx = x + dx[index] 
            ny = y + dy[index]

            # 불필요한 코드 중복이 너무 많다...
            # if nx < 0 or ny < 0 or nx >= r or ny >= c: # 먑 벆울 벗어났을 경우
            #     continue

            # if yard[nx][ny] == "#":
            #     continue

            # if not visited[nx][ny] and yard[nx][ny] == "v":
            #     wolf_count += 1  
            #     visited[nx][ny] = True
            #     queue.append([nx, ny])
            # elif not visited[nx][ny] and yard[nx][ny] == "o":
            #     sheep_count += 1
            #     visited[nx][ny] = True
            #     queue.append([nx, ny])
            # elif not visited[nx][ny] and yard[nx][ny] == ".":
            #     visited[nx][ny] = True
            #     queue.append([nx, ny])

            # 먑 벆울 벗어났지 않고, 울타리가 아닐 경우, 방문하지 않았을 경우
            if 0 <= nx < r and 0 <= ny < c and yard[nx][ny] != "#" and not visited[nx][ny]: 
                
                if yard[nx][ny] == "v":
                    wolf_count += 1  
                
                elif yard[nx][ny] == "o":
                    sheep_count += 1
                
                visited[nx][ny] = True
                queue.append([nx, ny])

    return wolf_count, sheep_count


r, c = map(int, input().split())

yard = [list(input()) for _ in range(r)] # 마당
visited = [[False] * c for _ in range(r)]

sheeps = 0 # 살아있는 양의 수
wolves = 0 # 살아있는 늑대의 수

for i in range(r):
    for j in range(c):
        if not visited[i][j] and (yard[i][j] == "v" or yard[i][j] == "o"):
            wolf_count, sheep_count = bfs(i, j)
            if wolf_count >= sheep_count: # 늑대가 양을 다 잡아먹을 경우
                wolves += wolf_count
            else: # 양이 늑대를 쫓아낼 경우
                sheeps += sheep_count

print(str(sheeps) + " " + str(wolves))