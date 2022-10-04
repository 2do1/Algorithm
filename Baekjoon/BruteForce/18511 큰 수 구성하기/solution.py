from itertools import product # 중복순열

n, k = map(int, input().split()) # n보다 같거나 작은 자연수, 집합 k의 원소 수

k_list = list(input().split())

answer = 0 # n보다 작거나 같은 자연수 중, k의 원소로만 구성된 가장 큰 수 

for i in range(1, len(str(n)) + 1):
    for num in list(product(k_list, repeat=i)):
        num = int(''.join(num))
        if num > answer and num <= n: # n보다 같거나 작고 가장 큰 수일 경우
            answer = num

print(answer)

# 시간 초과
# n, k = map(int, input().split()) # n보다 같거나 작은 자연수, 집합 k의 원소 수

# k_list = list(map(int, input().split()))

# answer = 0 # n보다 작거나 같은 자연수 중, k의 원소로만 구성된 가장 큰 수 
# for i in range(1, n + 1):
#     only_k = True # k의 원소로만 구성되어있는지 
#     num_list = list(str(i)) # 각 자릿 수 별로 쪼개준다.
#     for num in num_list:
#         num = int(num) # 문자열 -> 숫자로 변환
#         if num not in k_list: # k의 원소가 아닐 경우
#             only_k = False
#             break

#     if only_k: # k의 원소로만 구성되어있을 경우
#         answer = i
#     else: # k의 원소로만 구성되어있지 않을 경우
#         continue
    
# print(answer)