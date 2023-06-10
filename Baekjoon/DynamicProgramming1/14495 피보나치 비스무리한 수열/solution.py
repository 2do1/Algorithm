n = int(input())

dp = [1] * 117

for index in range(4, n + 1):
    dp[index] = dp[index - 1] + dp[index - 3]

print(dp[n])