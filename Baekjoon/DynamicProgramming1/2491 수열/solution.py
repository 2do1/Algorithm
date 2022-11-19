n = int(input()) 

nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    if nums[i] >= nums[i - 1]:
        dp[i] = dp[i - 1] + 1
        continue
    dp[i] = 1

dp2 = [0] * n
dp2[0] = 1

for i in range(1, n):
    if nums[i] <= nums[i - 1]:
        dp2[i] = dp2[i - 1] + 1
        continue
    dp2[i] = 1

print(max(max(dp), max(dp2)))

# 다른 풀이
# import sys
# input  = sys.stdin.readline

# n = int(input())
# num = list(map(int,input().split()))

# #dp: i번째까지 왔을때 수열의 최대 길이-증가할때/감소할때 
# d = [[1]*n for _ in range(2)]

# for i in range(1,n):
#     if num[i-1]<=num[i]: #증가할경우
#         d[0][i] = d[0][i-1]+1                         
#     if num[i-1]>=num[i]: #감소할경우
#         d[1][i] = d[1][i-1]+1
# print(max(map(max,d)))