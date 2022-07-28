n = int(input()) # 길이가 N

num_list = list(map(int, input().split())) # 수열 A

prime_num_list = [] # 소수들
for num in num_list:
    prime_num = True # 소수인지의 여부
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: # 소수가 아닐 경우
            prime_num = False
            break
    
    if prime_num and num not in prime_num_list: # 소수일 경우, 이전에 나온 소수가 아닐 경우
        prime_num_list.append(num)


if len(prime_num_list) == 0: # 소수기 없을 경우
    print(-1)
else: # 소수가 있을경우
    lcm = 1 # 소수들의 최소공배수
    for num in prime_num_list:
        lcm *= num
    print(lcm)
