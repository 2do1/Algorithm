def euclid(a, b): # 최대공약수 
    if a < b: # b가 a보다 크면
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split()) # 두 자연수

gcd = euclid(a, b) # 최대공약수
lcm = (a // gcd) * (b // gcd) * gcd # 최소공배수

print(gcd)
print(lcm)