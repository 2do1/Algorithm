# m 이상 n 이하의 자연수 중 소수인 것
m = int(input()) 
n = int(input())

prime_num_list = [] # 소수를 담을 리스트

for i in range(m, n + 1): # m 이상 n 이하의 자연수
    prime_num = True # 소수인지의 여부를 알려주는 변수
    if i > 1: # 숫자 1보다 클 경우에만 소수인지 검사
        for j in range(2, i // 2 + 1): # 소수 판별
            if i % j == 0: # 소수가 아닐 경우
                prime_num = False
                break
        if prime_num: # 소수라면
            prime_num_list.append(i)

if len(prime_num_list) == 0: # m 이상 n 이하의 자연수 중 소수가 없을 경우
    print(-1)
else: # 소수가 있을 경우
    print(sum(prime_num_list)) # 모든 소수의 합
    print(min(prime_num_list)) # 모든 소수중 최솟값