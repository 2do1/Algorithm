from itertools import combinations

def gcd(a, b): # 최대공약수
    if a < b: # b가 a보다 크면
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    answer = 0 # 모든 쌍의 GCD의 합
    num_list = list(map(int, input().split())) # n개의 수
    num_list = num_list[1:] # 0번째 인덱스는 수의 개수인 n을 의미하므로

    case_list = list(combinations(num_list, 2)) # 두 숫자를 뽑을 수 있는 모든 경우의 수 
    for case in case_list:
        a, b = case
        temp = gcd(a, b) # 최대공약수
        answer += temp

    print(answer)

# 다른 사람의 풀이
# import sys
# import math
# n=int(input())

# for i in range(n):
#     arr=list(map(int, sys.stdin.readline().split()))
#     total=0
#     for j in range(1,len(arr)):
#         for k in range(j+1,len(arr)):
#             total+=math.gcd(arr[j],arr[k])
#     print(total)