from itertools import combinations

def solution(nums):
    answer = 0
    case_list = list(combinations(nums, 3)) # 서로 다른 3개를 뽑는 모든 경우의 수
    
    for case in case_list:
        total = sum(case) # 서로 다른 3개를 골라 모두 더한 값
        prime_num = True # 소수인지의 여부
        for i in range(2, int(total ** 0.5) + 1):
            if total % i == 0: # 소수가 아닐 경우
                prime_num = False
                break
        
        if prime_num: # 소수일 경우
            answer += 1            

    return answer

# 2440번
n = int(input()) # 별 n개
for i in range(n, 0, -1):
    print('*' * i)