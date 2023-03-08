n = int(input())

stairs = [0] + [int(input()) for _ in range(n)]

# 0번째는 시작점
dp = [0] * (n + 1)
if n == 1:
    print(stairs[1])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for index in range(3, n + 1):
        dp[index] = max(dp[index - 2], dp[index - 3] + stairs[index - 1]) + stairs[index]

print(dp[n])