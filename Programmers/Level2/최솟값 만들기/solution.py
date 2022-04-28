def solution(A,B):
    answer = 0 
#     for i in range(len(A)):
#         min_a = min(A)
#         max_b = max(B)
#         answer += min_a * max_b
#         A.remove(min_a)
#         B.remove(max_b)
    
    # 한 리스트에서는 최댓값, 다른 한 리스트에서는 최솟값을 뽑아오자.
    A.sort() # 오름차순 정렬 
    B.sort(reverse=True) # 내림차순 정렬 
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer