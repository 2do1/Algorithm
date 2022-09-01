# 탑 다운, 피보나치 수열 재귀적 구현

dp = [0] * 100 # 메모이제이션 하기 위한 리스트 

def fibo(x):
    if x == 1 or x == 2: # 재귀 함수 종료 조건
        return 1 

    if dp[x] != 0: # 이미 기록을 한, 계산한 값이라면
        return dp[x] # 그대로 반환
    else: # 계산한 값이 아니라면
        dp[x] = fibo(x - 1) + fibo(x - 2) # 기록 후 
        return dp[x] # 반환

print(fibo(99))

# 바텀 업, 피보나치 수열 반복적 구현

dp = [0] * 100 # dp 테이블 초기화

dp[1] = 1
dp[2] = 1
n = 99

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])