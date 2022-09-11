n = int(input()) # 식량 창고의 개수

food_list = list(map(int, input().split())) # 각 식량창고에 저장된 식량의 개수 

dp = [0] * (n + 1) # dp 테이블
dp[0] = food_list[0]
dp[1] = max(food_list[0], food_list[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], food_list[i] + dp[i - 2])

print(dp[n - 1])