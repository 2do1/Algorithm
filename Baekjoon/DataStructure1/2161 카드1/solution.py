from collections import deque

n = int(input())

nums = [num for num in range(1, n + 1)]

queue = deque(nums)

while len(queue) != 1:
    print(queue.popleft(), end=" ")
    queue.append(queue.popleft())

print(queue[0])