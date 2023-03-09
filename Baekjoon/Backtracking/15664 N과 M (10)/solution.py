n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))
visited = [False] * n
stack = []

def dfs(num):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    pre = 0
    for index in range(num, n):
        if not visited[index] and pre != numbers[index]: 
            stack.append(numbers[index])
            pre = numbers[index]
            visited[index] = True
            dfs(index + 1)
            stack.pop()
            visited[index] = False

dfs(0)