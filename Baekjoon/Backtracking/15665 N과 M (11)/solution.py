n, m = map(int, input().split())

numbers = sorted(map(int , input().split()))
stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    pre = 0
    for index in range(n):
        if pre != numbers[index]:
            stack.append(numbers[index])
            pre = numbers[index]
            dfs()
            stack.pop()

dfs()