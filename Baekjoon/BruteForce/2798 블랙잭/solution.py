from itertools import combinations

 # n은 카드 개수, m은 숫자
n, m = map(int, input().split())

card_list = list(map(int, input().split())) # 카드 종류 담을 리스트

pick_cases = list(combinations(card_list, 3)) # 3장의 카드를 고를 경우의 수 

answer = 0
for case in pick_cases:
    case_sum = sum(case)
    if answer < case_sum and case_sum <= m: # 합이 숫자 m 이하이고, 이전 경우의수보다 클 때
        answer = case_sum

print(answer)