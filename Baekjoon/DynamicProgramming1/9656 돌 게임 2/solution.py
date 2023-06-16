n = int(input()) # 돌 n개

dp = [-1] * 1001 # dp 테이블 초기화

dp[1] = 0 # 창영이 승리
dp[2] = 1 # 상근이 승리
dp[3] = 0

for i in range(4, n + 1):
    if dp[i - 1] == 1 or dp[i - 3] == 1: 
        dp[i] = 0
    else: 
        dp[i] = 1

if dp[n] == 1: # 상근이 승리일 경우
    print("SK")
else: # 창영이 승리일 경우
    print("CY")

# 간단한 풀이
# N = int(input())
# print("CY" if N % 2 else "SK")