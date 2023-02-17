n = int(input())

board = [list(input()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)]

# 12시부터 시계방향으로 
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(n):
    play = list(input())
    for j in range(len(play)):
        if play[j] == 'x': # 열린 칸일 경우
            if board[i][j] == '*': # 지뢰를 밟았을 경우
                for k in range(n):
                    for l in range(n):
                        if board[k][l] == '*':
                            answer[k][l] = '*'
                            
            else: # 지뢰를 밟지 않았을 경우
                count = 0
                for k in range(8):
                    x = i + dx[k] 
                    y = j + dy[k]

                    if x < 0 or y < 0 or x >= n or y >= len(play): # 맵 밖으로 벗어났을 경우
                        continue
                
                    if board[x][y] == '*': # 지뢰일 경우 
                        count += 1
            
                answer[i][j] = (str(count))

            
        else: # "." 열리지 않은 칸일 경우
            if answer [i][j] == '*': # 지뢰일 경우 넘어간다.
                continue
            answer[i][j] = '.'

for index in range(n):
    print("".join(answer[index]))