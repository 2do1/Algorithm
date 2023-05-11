n = int(input())
find_num = int(input())

graph = [[0] * n for _ in range(n)]

max_num = n * n
x = -1
y = 0

while max_num:
    for _ in range(n):
        x += 1
        graph[x][y] = max_num
        max_num -= 1

    n -= 1
    for _ in range(n):
        y += 1
        graph[x][y] = max_num
        max_num -= 1
    
    for _ in range(n):
        x -= 1
        graph[x][y] = max_num
        max_num -= 1

    n -= 1
    for _ in range(n):
        y -= 1
        graph[x][y] = max_num
        max_num -= 1


for row in graph:
    print(*row)

for index, row in enumerate(graph):
    if find_num in row:
        print(index + 1, row.index(find_num) + 1)