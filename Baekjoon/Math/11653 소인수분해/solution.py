n = int(input())

if n == 1: # n이 1일 경우
    pass # 아무것도 출력 하지 않는다.
else: # n이 1이 아닐 경우
    i = 2
    while n != 1 : # n이 1이 될 때 까지
        if n % i == 0: # 나누어질 경우
            n //= i
            print(i) # 소인수 분해 결과 출력
        else:
            i += 1