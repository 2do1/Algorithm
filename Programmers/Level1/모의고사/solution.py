
def solution(answers):
    answer = []
    
    score_list = [0, 0, 0] # 문제를 맞친 횟수
    num1 = [1, 2, 3, 4, 5] # 수포자 1
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] # 수포자 2
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 수포자 3
    
    # # enumerate() 함수 사용
    # for idx, answer in enumerate(answers):
    #     if answer == pattern1[idx%len(pattern1)]:
    #         score[0] += 1
    #     if answer == pattern2[idx%len(pattern2)]:
    #         score[1] += 1
    #     if answer == pattern3[idx%len(pattern3)]:
    #         score[2] += 1
            
    for i in range(len(answers)): 
        if answers[i] == num1[i % len(num1)]: # 수포자1이 정답을 맞췄을 경우
            score_list[0] += 1
        if answers[i] == num2[i % len(num2)]: # 수포자2가 정답을 맞췄을 경우
            score_list[1] += 1
        if answers[i] == num3[i % len(num3)]: # 수포자3이 정답을 맞췄을 경우
            score_list[2] += 1
            
    for i in range(len(score_list)):
        if score_list[i] == max(score_list): # 가장 높은 점수 일 경우
            answer.append(i + 1) 
    
    return answer