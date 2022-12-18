def gcd(a, b): # 최대공약수
    if a < b: # b가 a보다 크면
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
a_list = list(map(int, input().split()))
x = int(input())

disjoints = []

for a in a_list:
    if gcd(a, x) == 1:
        disjoints.append(a)

print(sum(disjoints) / len(disjoints))