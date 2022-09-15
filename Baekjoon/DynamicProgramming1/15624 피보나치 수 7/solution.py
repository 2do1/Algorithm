n = int(input()) # n번째 피보나치 수 

dp = [0] * 1000001 # dp 테이블 초기화
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

print(dp[n])

# 메모리 초과
# n = int(input()) # n번째 피보나치 수 

# dp = [0] * (n + 1) # dp 테이블 초기화
# dp[1] = 1

# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n] % 1000000007)