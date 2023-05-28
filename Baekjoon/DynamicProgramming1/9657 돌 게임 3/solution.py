n = int(input()) # 돌 N개

dp = [0, 1, 0, 1, 1] + [0] * (n - 4)


for index in range(5, n + 1):
    if dp[index - 4] == 0 or dp[index - 3] == 0 or dp[index - 1] == 0:
        dp[index] = 1
    else:
        dp[index] = 0

if dp[n]: # 1일 경우 상근이 승리
    print("SK")
else: # 0일 경우 창영이 승리
    print("CY")