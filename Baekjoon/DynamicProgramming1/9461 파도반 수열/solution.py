t = int(input()) # 테스트 케이스의 개수

for _ in range(t):
    n = int(input()) # 숫자 n

    dp = [0] * 101 # dp 테이블 초기화
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    print(dp[n])