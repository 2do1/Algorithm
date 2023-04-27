## itertools 모듈을 이용한 풀이
from itertools import product

def solution(word):
    answer = 0
    
    alphabets = ['A', 'E', 'I', 'O', 'U']
    cases = set()
    
    for length in range(1, len(alphabets) + 1):
        for case in product(alphabets, repeat=length):
            case = ''.join(case)
            cases.add(case)

    cases = sorted(cases)
    answer = cases.index(word) + 1
    
    return answer

## DFS 풀이 
# def solution(word):
#     answer = 0
#     word_list = []
#     words = 'AEIOU'
    
#     def dfs(cnt, w):
#         if cnt == 5:
#             return 
#         for i in range(len(words)):
#             word_list.append(w + words[i])
#             dfs(cnt+1, w + words[i])
            
#     dfs(0,"")
    
#     return word_list.index(word)+1