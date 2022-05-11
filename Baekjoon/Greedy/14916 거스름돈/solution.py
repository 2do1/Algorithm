n = int(input()) # n, 거스름돈 액수 

# 동전 종류 5원, 2원
min_coin_count = 0 # 거스름돈 동전의 최소 개수
change = False # 거슬러 줄 수 있는지의 여부

if n % 5 == 0: # 5원짜리로 다 거슬러 줄 수 있는 경우
    min_coin_count += n // 5
    change = True
else:
    quotient = n // 5 # 5원으로 최대한 거슬러 줄 수 있는 개수.
    temp = n # 임시 변수에 거스름돈 액수 저장
    for i in range(quotient, -1, -1): # 최대 개수 ~ 0까지 
        n -= i * 5
        if n % 2 == 0: 
            min_coin_count += i # 5원 짜리 동전 개수
            min_coin_count += n // 2 # 2원 짜리 동전 개수
            change = True 
            break
        else:
            n = temp # 거스름돈 액수로 다시 초기화
            continue

if change: # 거슬러 줄 수 있는 경우
    print(min_coin_count)
else: # 거슬러 줄 수 없는 경우
    print(-1)

# 다른 사람 풀이1 (그리디)
# min_coin_count = 0 

# while True:
#     if n % 5 == 0: # 5의 배수이면 또는 2로만 거슬러준 경우 
#         min_coin_count += n // 5
#         break
#     else: # 5의 배수가 아니면 2씩 빼면서 5로 나누어 떨어지는것이 나오도록
#         n -= 2
#         min_coin_count += 1
    
#     if n < 0: # 거슬러 줄 수 없음을 의미한다
#         break

# if n < 0: # 거슬러 줄 수 없을 경우 
#     print(-1)
# else: # 거슬러 줄 수 있는 경우
#     print(min_coin_count)

# 다른 사람 풀이2 (DP)
# 2원짜리 동전의 개수는 똑같은 패턴이 반복
# 5원짜리 동전은 다섯 번째 이전의 dp 값에서 하나만 더 사용해주면 된다. 
# n = int(input())
# dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]
# for i in range(10,n+1):
#     dp.append(dp[i-5]+1)

# print(dp[n])