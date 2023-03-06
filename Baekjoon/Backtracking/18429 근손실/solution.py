# def dfs(total_weight, depth):
#     global answer

#     if depth == n:
#         answer += 1
#         return
    
#     for index in range(n):
#         if not visited[index] and total_weight + weights[index] - k >= 500:
#             visited[index] = True
#             total_weight += weights[index] - k
#             dfs(total_weight, depth + 1)
#             visited[index] = False
#             total_weight -= weights[index] - k

def dfs(total_weight, depth):
    global answer

    if depth == n:
        answer += 1
        return
    
    for index in range(n):
        if not visited[index] and total_weight + weights[index] - k >= 500:
            visited[index] = True
            dfs(total_weight + weights[index] - k, depth + 1)
            visited[index] = False
            

n, k = map(int, input().split())

weights = list(map(int, input().split()))
visited = [False] * (n + 1)

answer = 0 # 500 이상이 되도록 하는 경우의 수

dfs(500, 0)
print(answer)