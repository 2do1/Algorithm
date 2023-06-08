base_radix = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())

answer = ""

while n != 0:
    answer += str(base_radix[n % b])
    n //= b

print(answer[::-1])