n = int(input())

romas = [1, 5, 10, 50]

answer = [] 
stack = []

def dfs(start):
    if len(stack) == n:
        if sum(stack) not in answer:
            answer.append(sum(stack))
        return

    for index in range(start, len(romas)):
        stack.append(romas[index])
        dfs(index)
        stack.pop()

dfs(0)

print(len(answer))