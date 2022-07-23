from itertools import permutations

n = int(input()) # n장의 카드
k = int(input()) # k개를 선택

answer = [] # 만들 수 있는 정수

card_list = [input() for _ in range(n)] # 카드
case_list = list(permutations(card_list, k)) # 순열, n개의 카드 중 k개를 중복 허용하지 않고 뽑아 나열한다.

for case in case_list:
    num = "".join(case) # 만든 정수
    if num not in answer: # 이미 만든 정수가 아닐 경우, 중복 제거
        answer.append(num)

print(len(answer)) # 만들 수 있는 정수의 개수