n = int(input())

numbers = list(map(int, input().split()))
visited = [False] * n
stack = []
answer = 0

def dfs():
    global answer
    if len(stack) == n: 
        total = 0 
        for index in range(n - 1):
            total += abs(stack[index] - stack[index + 1])
        answer = max(answer, total)
        return
    
    for index in range(n):
        if not visited[index]:
            stack.append(numbers[index])
            visited[index] = True
            dfs()
            stack.pop()
            visited[index] = False

dfs()

print(answer)