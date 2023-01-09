n = int(input())

answer = []
for num in range(1, n + 1):
    total = [n, num]
    while True:
        temp = total[-2] - total[-1]
        if temp < 0:
            if len(total) > len(answer):
                answer = total
            break
        total.append(temp)
        
print(len(answer))
print(*answer)