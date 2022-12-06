n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))
stack = []

def dfs(start):
    if len(stack) == m: # 길이가 m인 수열일 경우
        print(' '.join(map(str, stack)))
        return

    for index in range(start, n):
        if numbers[index] not in stack: # 스택에 들어있지 않을 경우
            stack.append(numbers[index])
            dfs(index + 1)
            stack.pop()

dfs(0)