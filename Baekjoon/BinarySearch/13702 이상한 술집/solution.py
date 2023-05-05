n, k = map(int, input().split())

kettles = [int(input()) for _ in range(n)]

start = 1
end = max(kettles)

answer = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for kettle in kettles:
        cnt += kettle // mid

    if cnt >= k:
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)