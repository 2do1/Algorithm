# 처음 내 풀이
def solution(want, number, discount):
    answer = 0
    
    total_want = []
    
    for w, num in zip(want, number):
        for _ in range(num):
            total_want.append(w)
    
    for i in range(len(discount) - 9):
        total_want_copy = total_want.copy()
        for j in range(i, i + 10):
            if discount[j] in total_want_copy and total_want_copy:
                total_want_copy.remove(discount[j])
        
        if not total_want_copy:
            answer += 1
            
    return answer

# Counter를 이용한 풀이
# from collections import Counter

# def solution(want, number, discount):
#     answer = 0
#     check = {}
#     for w, n in zip(want, number):
#         check[w] = n
    
#     for i in range(len(discount)-9):
#         c = Counter(discount[i:i+10])
#         if c == check:
#             answer += 1

#     return answer