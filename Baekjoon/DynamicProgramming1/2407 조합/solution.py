n, m = map(int, input().split()) 

dp = [[0] * 101 for _ in range(101)]

for i in range(n + 1):
    for j in range(i + 1):
        if i == j or j == 0: # nCn이나 nC0일 경우
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][m])