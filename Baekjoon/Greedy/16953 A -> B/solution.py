import sys

a, b = map(int, sys.stdin.readline().split())

answer = 1
while b > a:
    if str(b)[-1] != "1" and b % 2 != 0:
        break

    if b % 2 == 0:
        b //= 2

    elif str(b)[-1] == "1":
        b = str(b)
        b = b[:len(b) - 1]
        b = int(b)
    
    answer += 1
    if a == b:
        break

if a == b:
    print(answer)
else:
    print(-1)