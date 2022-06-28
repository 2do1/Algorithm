import sys

t = int(sys.stdin.readline().strip()) # 테스트 케이스 개수

for _ in range(t):
    answer = 0 # 문제의 조건을 만족하는 (a, b) 쌍의 개수
    # 0 < a < b < n 인 정수 a, b
    n, m = map(int, sys.stdin.readline().split())
    
    for a in range(1, n - 1): # a -> 1 ~ n - 2 까지
        for b in range(a + 1, n): # b -> a + 1 ~ n - 1 까지
            if (a ** 2 + b ** 2 + m) % (a * b) == 0: # 문제 조건
                answer += 1
                
    print(answer)

# 시간 초과
# t = int(input()) # 테스트 케이스 개수

# for _ in range(t):
#     answer = 0 # 문제의 조건을 만족하는 (a, b) 쌍의 개수
#     # 0 < a < b < n 인 정수 a, b
#     n, m = map(int, input().split())
    
#     for a in range(1, n - 1): # a -> 1 ~ n - 2 까지
#         for b in range(a + 1, n): # b -> a + 1 ~ n - 1 까지
#             result = (a ** 2 + b ** 2 + m) / (a * b) # 문제 조건
#             if result == int(result): # 값이 정수인 경우
#                 answer += 1
    
#     print(answer)

# 시간 초과
# from itertools import combinations
# t = int(input()) # 테스트 케이스 개수

# for _ in range(t):
#     answer = 0 # 문제의 조건을 만족하는 (a, b) 쌍의 개수
#     # 0 < a < b < n 인 정수 a, b
#     n, m = map(int, input().split())
#     n_list = [i for i in range(1, n)] # 1 ~ n - 1 까지의 정수
#     a_b_list = list(combinations(n_list, 2)) # 가능한 정수 쌍 (a, b)
    
#     for a_b in a_b_list:
#         a, b = a_b # 0번째 인덱스 -> a, 1번째 인덱스 -> b
        
#         result = (a ** 2 + b ** 2 + m) / (a * b) # 문제 조건
#         if result == int(result): # 값이 정수인 경우
#             answer += 1
    
#     print(answer)