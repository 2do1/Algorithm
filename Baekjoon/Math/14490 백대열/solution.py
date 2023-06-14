def gcd(a, b): # 최대공약수
    if a < b: # b가 a보다 크면
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split(':'))

g = gcd(n, m)
print("{0}:{1}".format(n // g, m // g))
