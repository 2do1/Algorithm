def is_prime_num(total):
    for index in range(2, int(total ** 0.5) + 1):
        if total % index == 0: # 소수일 경우
            return False
    return True

def dfs(num):
    if len(stack) == m: # 선별한 소의 수가 m개 일 경우
        total = sum(stack) # 소들의 몸무게 합
        if is_prime_num(total): # 소수일 경우
            answer.append(total)
        return
    
    for index in range(num, n):
        if not visited[index]:
            stack.append(cows[index])
            visited[index] = True
            dfs(index + 1)
            stack.pop()
            visited[index] = False

    

n, m = map(int, input().split())

cows = list(map(int, input().split()))
stack = []
visited = [False] * n
answer = []

dfs(0)

if not answer: # 경우가 없을 경우
    print(-1)
else:
    print(*sorted(set(answer)))