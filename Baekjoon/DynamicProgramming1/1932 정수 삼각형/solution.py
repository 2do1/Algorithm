# 처음 내 풀이
# n = int(input())

# tri = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(n):
#     for j in range(len(tri[i])):
#         dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + tri[i][j] # 오른쪽 대각선, 왼쪽 대각선


# answer = max(dp[n - 1])
# print(answer)

## 다른 사람들 풀이
n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(len(tri[i])):
        if j == 0: # 맨 왼쪽 끝일 경우
            dp[i][j] = dp[i - 1][j] + tri[i][j]
        elif i == j: # 맨 오른쪽 끝일 경우
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + tri[i][j]

answer = max(dp[n - 1])
print(answer)