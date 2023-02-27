n, m = map(int, input().split())

a = list(map(int, input().split()))

i, j = 0, 1

answer = 0
while i <= j and j <= n:

    total = sum(a[i:j]) # i부터 j번째 수까지의 합

    if total == m:
        answer += 1
        i += 1
    elif total > m:
        i += 1
    else:
        j += 1

print(answer)