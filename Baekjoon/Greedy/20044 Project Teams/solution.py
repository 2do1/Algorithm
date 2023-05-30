n = int(input())

w = sorted(map(int, input().split()))
w_reverse = sorted(w, reverse=True)

answer = 1e9

for index in range(n):
    total = w[index] + w_reverse[index]

    answer = min(answer, total)

print(answer)