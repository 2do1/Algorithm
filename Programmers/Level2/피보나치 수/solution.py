def solution(n):
    answer = 0
    
    dp = [0] * (n + 1) # dp 테이블 생성
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    answer = dp[n] % 1234567 # 나눈 나머지 리턴
    return answer

# 틀린 코드
# import sys

# sys.setrecursionlimit(5000) # 파이썬 재귀 횟수 제한 풀어주기

# def fibo(n):
#     if n == 0: # 0일 경우
#         return 0
#     if n == 1 or n == 2: # 1 또는 2일 경우
#         return 1
#     return fibo(n - 1) + fibo(n - 2)

# def solution(n):
#     answer = fibo(n) % 1234567
#     return answer
