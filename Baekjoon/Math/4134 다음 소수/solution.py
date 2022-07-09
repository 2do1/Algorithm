t = int(input()) # 테스트케이스

for _ in range(t):
    n = int(input()) # n보다 크거나 같은 소수 중 가장 작은 소수
    if n == 0 or n == 1: # 0 또는 1일 경우
        print(2)
        continue

    while True:
        prime_num = True # 소수인지의 여부
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: # 소수가 아닐 경우 
                prime_num = False
                n += 1 # 다음 숫자 확인
                break
        
        if prime_num: # 소수일 경우
            print(n)
            break