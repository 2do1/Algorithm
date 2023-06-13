n = int(input())

dp = [0] * 11
dp[1] = 0
dp[2] = 1

for index in range(3, n + 1):
    h = index // 2
    dp[index] = h * (index - h) + dp[h] + dp[index - h]

print(dp[n])