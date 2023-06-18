a, b = map(int, input().split())
n = int(input())

answer = abs(a - b)

likes = [int(input()) for _ in range(n)]

for like in likes:
    diff = abs(like - b)
    if answer > diff:
        answer = diff + 1

print(answer)