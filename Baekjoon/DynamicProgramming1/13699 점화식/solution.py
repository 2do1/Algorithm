n = int(input())

dp = [0] * 36 # dp 테이블 초기화
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[n])

# # IndexError
# n = int(input())

# dp = [0] * (n + 1) # dp 테이블 초기화
# dp[0] = 1
# dp[1] = 1

# for i in range(2, n + 1):
#     result = 0 # 점화식 결과
#     for j in range(i):
#         result += dp[j] * dp[i - j - 1]
#     dp[i] = result

# print(dp[n])