n = int(input())

ropes = sorted([int(input()) for _ in range(n)])

answer = 0 
for i in range(len(ropes)):
    total = ropes[i] * (len(ropes) - i) 
    answer = max(answer, total)

print(answer)