# 내풀이
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0: # 0, 짝수번째 인덱스일 경우
            answer += "수"
        else: # 홀수번째 인덱스일 경우
            answer += "박"
        
    return answer

# 다른 사람의 풀이1
# 슬라이싱 이용
# def solution(n):
#     answer = "수박" * n
        
#     return answer[:n]

# 다른 사람의 풀이2
# //, % 연산자 이용
# def solution(n):
#     answer = "수박" * (n//2) + "수" * (n%2)
        
#     return answer