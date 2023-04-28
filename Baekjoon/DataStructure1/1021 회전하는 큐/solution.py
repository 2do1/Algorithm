from collections import deque

n, m = map(int, input().split())
pick_numbers = list(map(int, input().split()))

queue = deque([i for i in range(1, n + 1)])

answer = 0 # 연산의 최솟값
for num in pick_numbers:
    
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        
        # 처음 내 조건
        # if queue.index(num) > abs(len(queue) - 1 - queue.index(num)):
        if queue.index(num) <= len(queue) // 2:
            queue.rotate(-1)
            answer += 1
        else:
            queue.rotate(1)
            answer += 1

print(answer)