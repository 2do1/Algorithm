n, m = map(int, input().split())

numbers = sorted(map(int, input().split()))
visited = [False] * n
stack = []

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    pre = 0 # 중복된 수 출력 방지 
    for index in range(n):
        if not visited[index] and pre != numbers[index]:
            pre = numbers[index]
            stack.append(numbers[index])
            visited[index] = True
            dfs()
            visited[index] = False
            stack.pop()

dfs()