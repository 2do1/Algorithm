n, s = map(int, input().split())

numbers = list(map(int, input().split()))
answer = 0 # 합이 S인 부분수열의 개수


def dfs(depth, total, count):
    global answer
    if depth == n: # 종료 조건, 재귀 깊이가 n일 경우
        if count > 0 and total == s: # 하나 이상 있을경우, 합이 s일 경우
            answer += 1
        return
    
    dfs(depth + 1, total + numbers[depth], count + 1) # 현재 수를 포함하는 경우
    dfs(depth + 1, total, count) # 현재 수를 포함하지 않는 경우

dfs(0, 0, 0)

print(answer) 