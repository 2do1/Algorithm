from itertools import combinations
n, m, k = map(int, input().split())

answer = 0

cases = list(combinations([num for num in range(n)], m))

for case in cases:
    count = 0

    for i in range(m):
        if case[i] < m:
            count += 1
    if count >= k:
        answer += 1

print(answer / len(cases))