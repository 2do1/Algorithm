n, a, d = map(int, input().split()) 

numbers = list(map(int, input().split()))

answer = 0
for index in range(len(numbers)):
    if numbers[index] == a:
        a += d
        answer += 1

print(answer)
        