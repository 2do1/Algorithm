def euclide(a, b): # 유클리드 호제법
    # while a != 0: # 반복문으로 구현
    #     tmp = b % a
    #     b = a
    #     a = tmp
    while a != 0:
        a, b = b % a, a
    return b

# def euclide(a, b): # 유클리드 호제법
#     if a == 0: # 재귀로 구현
#         return b
#     else:
#         return euclide(b % a, a)
    
t = int(input()) # 테스트케이스의 개수
for _ in range(t):
    a, b = map(int, input().split())
    gcd = euclide(a, b) # 최대공약수
    lcm = (a // gcd) * (b // gcd) * gcd # 최소공배수
    print(lcm)