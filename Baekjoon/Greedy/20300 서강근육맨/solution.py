n = int(input())

t = sorted(map(int, input().split()))

answer = 0

if len(t) % 2 != 0:
    for index in range(len(t) // 2):
        answer = max(answer, t[index] + t[n - index - 2])
else:
    for index in range(len(t) // 2):
        answer = max(answer, t[index] + t[n - index - 1])

print(answer)