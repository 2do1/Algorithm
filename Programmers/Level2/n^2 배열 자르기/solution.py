def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        num = max(i // n, i % n) + 1
        answer.append(num)
    
    return answer

# # 시간초과 발생
# def solution(n, left, right):
#     answer = []
    
#     array = [] # 과정대로 만들어진 1차원 배열
    
#     for i in range(n):
#         for j in range(n):
#             # 값이 더 큰 것들을 1차원 배열에 넣어준다.
#             if i > j:
#                 array.append(i + 1)
#             else:
#                 array.append(j + 1)
    
#     answer = array[left:right + 1]
#     return answer