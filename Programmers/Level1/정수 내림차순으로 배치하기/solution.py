def solution(n):
    answer = 0
    n = str(n)
    # n = map(str, str(n)) 처음 풀이. map() 함수를 이용하기 위해 문자열로 변환해주었다.
    
    n = sorted(n, reverse=True) # 내림차순으로 정렬 후 리스트로 리턴
    # n = list(str(n)) -> n.sort(reverse=True)
    
    answer = int(''.join(n)) # join() 함수로 문자열을 합쳐준 뒤 int형으로 변환해준다.
    return answer