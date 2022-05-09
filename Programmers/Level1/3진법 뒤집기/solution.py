def solution(n):
    answer = 0
    
    ternary = [] # 3진법
    while n != 0:
        ternary.append(n % 3)
        n //= 3
    
    # ternary.reverse() # 리스트 뒤집기
    # for i in range(len(ternary)):
    #     answer += ternary[i] * 3 ** i
    
    for i in range(len(ternary)): 
        answer += ternary[-i-1] * 3 ** i # 리스트 마지막에서부터 처음까지
    return answer

#     다른 사람의 풀이
#     ternary = "" # 3진법
    
#     while n != 0:
#         ternary += str(n % 3)
#         n //= 3
    
#     answer = int(ternary, 3) # 3진법으로 변환