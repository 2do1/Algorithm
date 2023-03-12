n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]


x, y = 0, 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 아래, 오른쪽, 오른쪽 아래
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maps[i - 1][j - 1]
        

print(dp[n][m])


# 처음 풀이
# n, m = map(int, input().split())

# maps = [list(map(int, input().split())) for _ in range(n)]

# dp = [[0] * (m + 1) for _ in range(n + 1)]


# x, y = 0, 0
# for i in range(n):
#     for j in range(m):
#         # 아래, 오른쪽, 오른쪽 아래
#         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maps[i][j]
        

# print(dp[n-1][m-1])