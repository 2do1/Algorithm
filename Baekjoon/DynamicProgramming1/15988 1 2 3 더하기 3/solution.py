import sys

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for index in range(4, 1000001):
    dp[index] = (dp[index - 1] + dp[index - 2] + dp[index - 3]) % 1000000009

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])