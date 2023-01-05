n = int(input())

times = sorted(map(int, input().split()))

answer = 0
for index in range(len(times)):
    answer += sum(times[:index + 1])

print(answer)