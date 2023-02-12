n = int(input())

dp = [0] * 91

dp[1] = 1
dp[2] = 1

for index in range(3, n + 1):
    dp[index] = dp[index - 1] + dp[index - 2]

print(dp[n])