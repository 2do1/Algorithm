n, m = map(int, input().split())

boards = [list(input()) for _ in range(n)]

answer = 2e9 # 다시 칠해야하는 정사각형 개수의 최솟값

# 가능한 모든 시작점 탐색
for i in range(n - 7):
    for j in range(m - 7): # 보드판 잘라준다. 
        w_start = 0 # W로 시작할 경우
        b_start = 0 # B로 시작할 경우
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0: # 시작점의 색깔과 같아야 한다.
                    if boards[k][l] != 'W':
                        w_start += 1
                    elif boards[k][l] != 'B':
                        b_start += 1   
                else: # 시작점의 색깔과 달라야 한다.
                    if boards[k][l] != 'B':
                        w_start += 1
                    elif boards[k][l] != 'W':
                        b_start += 1
        answer = min(answer, min(w_start, b_start))

print(answer)