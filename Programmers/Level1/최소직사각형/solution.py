def solution(sizes):
    answer = 0 # 가장 작은 지갑의 크기
    
    width = [] 
    height = [] 
    
    for size in sizes:
        width.append(max(size[0], size[1])) # 더 큰 애를 가로 리스트에
        height.append(min(size[0], size[1])) # 더 작은 애를 세로 리스트에

    answer = max(width) * max(height) # 제일 큰 값끼리 곱해준다.
    
    return answer