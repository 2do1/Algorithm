x, y = map(int, input().split())

z = y * 100 // x

answer = 0
start = 1
end = x

if x == y:
    print(-1)
elif z == 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
    
        if (y + mid) * 100 // (x + mid) <= z:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    print(answer)