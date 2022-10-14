n, m = map(int, input().split()) 

stack = []

def dfs(start):
    if len(stack) == m: # 길이가 m인 수열일 경우
        print(" ".join(map(str, stack)))
        return
    
    for i in range(start, n + 1):
        if i not in stack:
            stack.append(i)
            dfs(i + 1)
            stack.pop()

dfs(1)