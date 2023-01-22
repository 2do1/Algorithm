import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 1)

dp[1] = 1

for index in range(2, n + 1):
    temp = 1e9
    for j in range(1, int(index ** 0.5) + 1):
        temp = min(temp, dp[index - j ** 2])
    dp[index] = temp + 1

print(dp[n])