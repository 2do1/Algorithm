n = int(input())

dp = [0] * 81
dp[0] = 2
dp[1] = 4

for index in range(2, n + 1):
    dp[index] = dp[index - 1] + dp[index - 2]


print(dp[n])