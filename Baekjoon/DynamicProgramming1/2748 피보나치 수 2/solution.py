n = int(input()) # n번째 피보나치 수 

dp = [0] * (n + 1) # dp 테이블 생성

dp[0] = 0
dp[1] = 1
# dp[2] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n]) # n번째 피보나치 수 출력