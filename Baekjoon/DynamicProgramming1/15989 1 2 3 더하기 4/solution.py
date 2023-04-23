t = int(input())

dp = [1] * 10001 # 모든 수는 1로 다 표현할 수 있다.

for index in range(2, 10001):
    dp[index] += dp[index - 2]

for index in range(3, 10001):
    dp[index] += dp[index - 3] 

for _ in range(t):
    n = int(input())
    
    print(dp[n])