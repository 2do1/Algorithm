def dfs(num):
    if len(stack) == 6: # 6개를 골랐을 경우
        print(' '.join(map(str, stack)))
        return
    
    for index in range(num, k):
        if not visited[index]:
            stack.append(numbers[index])
            visited[index] = True
            dfs(index + 1)
            stack.pop()
            visited[index] = False


while True:
    numbers = list(map(int, input().split())) # 오름차순으로 주어 진다.

    if numbers == [0]: # 입력 마지막 줄일 경우
        break

    k = numbers[0] # k개의 수를 골라
    numbers = numbers[1:]

    stack = [] 
    visited = [False] * (k)
    dfs(0)
    print() # 빈줄 하나 출력