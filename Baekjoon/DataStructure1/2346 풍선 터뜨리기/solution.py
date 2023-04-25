from collections import deque

n = int(input())

balloons = enumerate(map(int, input().split()))

queue = deque(balloons)
answer = []

while queue:
    index, balloon = queue.popleft()

    answer.append(index + 1)

    if balloon > 0:
        queue.rotate(-(balloon - 1))
    elif balloon < 0:
        queue.rotate(-balloon)

for num in answer:
    print(num, end=' ')