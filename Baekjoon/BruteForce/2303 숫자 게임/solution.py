from itertools import combinations

n = int(input())

cards = [list(map(int, input().split())) for _ in range(n)]

answer = []
for index, card in enumerate(cards):
    score = 0
    for case in combinations(card, 3):
        total = sum(case) % 10
        score = max(score, total)
    
    answer.append([score, index + 1])


answer = sorted(answer, key=lambda x : (-x[0], -x[1]))

print(answer[0][1])