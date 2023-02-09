n = int(input())

numbers = sorted(map(int, input().split()))

x = int(input())

answer = 0
start = 0
end = n - 1

while start < end:
    if numbers[start] + numbers[end] == x:
        answer += 1
        start += 1
        end -= 1
    elif numbers[start] + numbers[end] > x:
        end -= 1
    else:
        start += 1

print(answer)