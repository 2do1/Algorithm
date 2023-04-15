n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n) for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0: # 갈 수 있는 경로라면
            
            if i == n - 1 and j == n - 1: # 마지막에 도착했을 경우
                break

            jump = board[i][j]
            if i + jump < n: # 맵 밖을 벗어나지 않았을 경우
                dp[i + jump][j] += dp[i][j]
        
            if j + jump < n: # 맵 밖을 벗어나지 않았을 경우
                dp[i][j + jump] += dp[i][j]

print(dp[n - 1][n - 1])