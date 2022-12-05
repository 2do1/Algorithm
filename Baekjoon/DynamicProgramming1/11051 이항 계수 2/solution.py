n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(i + 1):
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007

print(dp[n][k])        