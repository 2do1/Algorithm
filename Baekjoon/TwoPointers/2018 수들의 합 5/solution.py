n = int(input())

answer = 0
total, end = 0, 0 

for start in range(n):
    while total < n and end < n:
        total += end + 1
        end += 1

    if total == n:
        answer += 1

    total -= start + 1

print(answer)