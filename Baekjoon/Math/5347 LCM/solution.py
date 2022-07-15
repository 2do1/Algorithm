def euclid(a, b):
    if a < b: # b가 a보다 클 경우
        a, b = b, a
        
    while b != 0:
        a, b = b, a % b
    return a


n = int(input()) # 테스트케이스의 개수

for _ in range(n):
    a, b = map(int, input().split())
    gcd = euclid(a, b) # 최대공약수
    lcm = (a // gcd) * (b // gcd) * gcd # 최소공배수
    print(lcm)