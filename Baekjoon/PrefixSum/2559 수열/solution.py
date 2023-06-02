n, k = map(int, input().split())

numbers = list(map(int, input().split()))

answer = []
answer.append(sum(numbers[:k])) # sum을 한번만 이용한다.

for index in range(n - k):
    answer.append(answer[index] - numbers[index] + numbers[index + k])

print(max(answer))