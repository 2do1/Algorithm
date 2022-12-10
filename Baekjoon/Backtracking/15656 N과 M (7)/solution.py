n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))
stack = []

def dfs():
    if len(stack) == m: # 길이가 m인 수열일 경우
        print(' '.join(map(str, stack)))
        return

    for index in range(n):
        stack.append(numbers[index])
        dfs()
        stack.pop()

dfs()