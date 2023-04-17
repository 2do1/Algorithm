def solution(clothes):
    answer = 0
    
    kinds = {} # 딕셔너리 구조
    for cloth in clothes:
        if cloth[1] in kinds.keys(): # 이미 있는 종류일 경우
            kinds[cloth[1]].append(cloth[0])
        else:
            kinds[cloth[1]] = [cloth[0]]
    
    answer = 1
    for value in kinds.values():
        answer *= (len(value) + 1) # 현재 옷 종류에 대한 개수 + 현재 옷 종류를 입지 않을 경우
    
    return answer - 1 # 모두다 입지않은 경우는 제외한다.