cocktail_list = list(map(int, input().split()))

answer = 1 # 가장 맛있다고 느끼는 칵테일의 맛
odd = False # 홀수가 있는지의 여부

for cocktail in cocktail_list:
    if cocktail % 2 != 0: # 홀수일 경우
        answer *= cocktail
        odd = True

if odd: # 홀수가 있을 경우
    print(answer)
else: # 짝수만 존재할 경우
    print(cocktail_list[0] * cocktail_list[1] * cocktail_list[2])