n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))
stack = []

def dfs(start):
    if len(stack) == m: # 길이가 m인 수열일 경우
        print(' '.join(map(str, stack)))
        return

    for index in range(start, n):
        stack.append(numbers[index])
        dfs(index)
        stack.pop()

dfs(0)