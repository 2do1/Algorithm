t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    n = int(input()) # n 개의 정수
    n_list = list(map(int, input().split()))
    dp = [-1000] * 1001 # dp 테이블 초기화
    dp[1] = n_list[0]

    for i in range(2, n + 1):
        dp[i] = max(n_list[i - 1], dp[i - 1] + n_list[i - 1])


    print(max(dp)) # maximum subarray의 합

# 다른 풀이
t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    n = int(input()) # n 개의 정수
    n_list = list(map(int, input().split()))
    dp = [0] * n # dp 테이블 초기화
    dp[0] = n_list[0]

    for i in range(1, n):
        dp[i] = max(n_list[i], dp[i - 1] + n_list[i])


    print(max(dp)) # maximum subarray의 합
