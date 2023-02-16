n = int(input())

a = list(map(int, input().split()))

answer = 2
length = 2 # 지그재그 순열 최소 길이

for index in range(n - 2):
    if a[index] <= a[index + 1] and a[index + 1] <= a[index + 2]:
        length = 2
    elif a[index] >= a[index + 1] and a[index + 1] >= a[index + 2]:
        length = 2
    else:
        length += 1
    answer = max(answer, least_len)

print(answer)