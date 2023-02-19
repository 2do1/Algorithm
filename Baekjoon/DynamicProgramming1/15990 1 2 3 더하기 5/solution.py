import sys

t = int(sys.stdin.readline())

dp = [[0] * 3 for _ in range(100001)]
    
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for index in range(4, 100001):
    dp[index][0] = (dp[index - 1][1] + dp[index - 1][2]) % 1000000009
    dp[index][1] = (dp[index - 2][0] + dp[index - 2][2]) % 1000000009
    dp[index][2] = (dp[index - 3][0] + dp[index - 3][1]) % 1000000009

for _ in range(t):
    n = int(sys.stdin.readline())

    print(sum(dp[n]) % 1000000009)