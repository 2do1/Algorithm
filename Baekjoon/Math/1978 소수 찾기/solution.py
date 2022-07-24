n = int(input()) # 주어진 수 N개
num_list = list(map(int, input().split())) # 주어진 수들

answer = 0 # 소수의 개수
for num in num_list:
    if num == 0 or num == 1: # 0 또는 1일 경우
        continue
    else:
        prime_num = True # 소수인지의 여부
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0: # 소수가 아닐 경우
                prime_num = False
                break
    
        if prime_num: # 소수일 경우
            answer += 1    
print(answer)