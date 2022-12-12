n, m = map(int, input().split())

chicken_prefer = [list(map(int, input().split())) for _ in range(n)]

answer = 0 
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            total = 0
            for l in range(n):
                total += max(chicken_prefer[l][i], chicken_prefer[l][j], chicken_prefer[l][k])
            
            answer = max(answer, total)

print(answer)

# 다른 풀이
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, m = map(int, input().split())
# like = [list(map(int, input().split())) for _ in range(n)]

# maxSum = 0
# for a, b, c in combinations(range(m), 3):
#     tmpSum = 0
#     for i in range(n):
#         tmpSum += max(like[i][a], like[i][b], like[i][c])
#     maxSum = max(maxSum, tmpSum)

# print(maxSum)