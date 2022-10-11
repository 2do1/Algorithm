n, m = map(int, input().split()) # 1부터 n까지 자연수 중 중복 없이 m개를 고른 수열

stack = [] # 스택

def dfs():
    if len(stack) == m: # 길이가 m인 수열일 경우
        print(' '.join(map(str, stack)))
        return

    for i in range(1, n + 1):
        if i not in stack: # 스택에 들어있지 않을 경우
            stack.append(i)
            dfs()
            stack.pop()

dfs()