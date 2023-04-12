from collections import deque

def solution(elements):
    answer = 0
    
    queue = deque(elements) # 덱 자료구조 이용
    cases = set() # 중복 제거를 위해 집합 자료구조 이용
    
    for i in range(1, len(elements) + 1):
        for _ in range(len(elements)):
            total = sum(list(queue)[:i]) # 리스트로 변환한뒤 슬라이싱을 통해 수열을 구하고 합을 구함
            cases.add(total)
            queue.rotate(1)
    
    answer = len(cases)
    
    return answer