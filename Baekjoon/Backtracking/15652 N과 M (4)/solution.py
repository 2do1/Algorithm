n, m = map(int, input().split())

stack = []

def dfs(start):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    for num in range(start, n + 1):
        stack.append(num)
        dfs(num)
        stack.pop()

dfs(1)