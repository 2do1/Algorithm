from itertools import permutations

def check_strike_ball(num):
    for question in questions:
        question_num = question[0] # 민혁이가 물어본 수
        question_num = str(question_num)

        strike = 0 # 스트라이크 개수
        ball = 0 # 볼 개수

        for index in range(3):
            if question_num[index] in num: # 숫자가 있을 경우
                if question_num[index] == num[index]: # 스트라이크일 경우
                    strike += 1
                else: # 볼일 경우
                    ball += 1

        if strike != question[1] or ball != question[2]:
            return False
        
    return True

n = int(input()) # 질문 개수

questions = [list(map(int, input().split())) for _ in range(n)]
answer = 0 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for case in (permutations(numbers, 3)):
    num = ""
    for index in range(len(case)):
        num += str(case[index])

    if check_strike_ball(num):
        answer += 1

print(answer)