n = int(input()) # n일

table = [list(map(int, input().split())) for _ in range(n)] # 상담 일정표

dp = [0] * 16 # dp 테이블 초기화

for i in range(n - 1, -1, -1):
    time = table[i][0] # 상담을 하는데 필요한 기간
    profit = table[i][1] # 상담할 때 받을 수 있는 금액
    if i + time > n: # 회사에 없는 날일 경우
        dp[i] = dp[i + 1]
    else: # 회사에 있는 날일 경우
        dp[i] = max(dp[i + 1], dp[i + time] + profit)
    
    # print(dp[i])

print(dp[0])