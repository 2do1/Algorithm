t = int(input())

dp = [[0, 0] for _ in range(41)]

dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for index in range(2, 41):
    dp[index][0] = dp[index - 1][0] + dp[index - 2][0]
    dp[index][1] = dp[index - 1][1] + dp[index - 2][1]

for _ in range(t):
    n = int(input())

    print(" ".join(map(str, dp[n])))