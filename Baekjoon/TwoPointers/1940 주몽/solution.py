n = int(input())
m = int(input())

numbers = sorted(map(int, input().split()))

start, end = 0, n - 1
answer = 0


while start < end:

    if numbers[start] + numbers[end] == m:
        answer += 1
        start += 1
        end -= 1
    elif numbers[start] + numbers[end] > m:
        end -= 1
    else:
        start += 1

print(answer)