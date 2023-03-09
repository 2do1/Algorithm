n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))

stack = []

def dfs(num):
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return

    pre = 0
    for index in range(num, n):
        if numbers[index] != pre:
            stack.append(numbers[index])
            pre = numbers[index]
            dfs(index)
            stack.pop()

dfs(0)