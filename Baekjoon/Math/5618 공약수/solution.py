# Python3에서는 시간초과
n = int(input()) # 자연수 n개

num_list = list(map(int, input().split())) # n개의 수
common_divisor = [] # 공약수

min_num = min(num_list) # 가장 작은 수

for i in range(1, min_num + 1):
    if min_num % i == 0: # 약수일 경우
        divisor = True # 공약수인지의 여부를 알려주는 변수

        for num in num_list:
            if num % i != 0: # 약수가 아닐 경우
                divisor = False
                break
        
        if divisor: # 공약수일 경우
            common_divisor.append(i)


for divisor in common_divisor:
    print(divisor)

# # Python3에서 시간초과 나지 않는 코드
# def gcd(a, b): # 최대공약수
#     if a == 0:
#         return b
#     return gcd(b % a, a)

# n = int(input())
# num_list = list(map(int, input().split()))
# common_divisor = gcd(num_list[0], gcd(num_list[1], num_list[-1]))

# for i in range(1, common_divisor // 2 + 1):
#     if common_divisor % i == 0:
#         print(i)

# print(common_divisor)