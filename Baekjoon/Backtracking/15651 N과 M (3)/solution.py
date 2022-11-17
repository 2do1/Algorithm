n, m = map(int, input().split())

stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    

    for num in range(1, n + 1):
        stack.append(num)
        dfs()
        stack.pop()

dfs()