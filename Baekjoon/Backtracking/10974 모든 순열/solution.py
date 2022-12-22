n = int(input())

stack = []

def dfs():
    if len(stack) == n:
        print(' '.join(map(str, stack)))
        return

    for num in range(1, n + 1):
        if num not in stack: 
            stack.append(num)
            dfs()
            stack.pop()
dfs()