from itertools import combinations

n = int(input())

ingredients = [list(map(int, input().split())) for _ in range(n)]

answer = 100000000001
for i in range(1, n + 1):
    for case in combinations(ingredients, i):
        sour = 1 # 신맛
        bitter = 0 # 쓴맛
        for j in range(len(case)):
            sour *= case[j][0]
            bitter += case[j][1]
        
        diff = abs(sour - bitter)
        answer = min(diff, answer)

print(answer)