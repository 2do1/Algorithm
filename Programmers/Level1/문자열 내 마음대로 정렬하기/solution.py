def solution(strings, n):
    answer = []
    # 인덱스 값을 기준으로 오름차순으로 정렬하고, 같다면 사전순으로 정렬
    answer = sorted(strings, key=lambda x: (x[n], x))
    
    return answer